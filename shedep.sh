#!/bin/bash

# Define the connection details
remote_hosts=("52.207.78.146" "35.175.64.54")
remote_user="ubuntu"
archive_path="./versions/web_static_$(date -u +"%Y%m%d%H%M%S").tgz"

function do_pack {
    # Create a tar gzipped archive of the directory web_static
    if [ ! -d "./versions" ]; then
        mkdir -p "./versions"
    fi
    tar -czf "${archive_path}" web_static
    echo "${archive_path}"
}

function do_deploy {
    # Distributes an archive to a web server
    archive_path=$1
    if [ ! -f "${archive_path}" ]; then
        return 1
    fi
    file=$(basename "${archive_path}")
    name="${file%.*}"
    for host in "${remote_hosts[@]}"; do
        scp "${archive_path}" "${remote_user}@${host}:/tmp/${file}"
        ssh "${remote_user}@${host}" "sudo rm -rf /data/web_static/*" \
            && ssh "${remote_user}@${host}" "sudo mkdir -p /data/web_static/releases/${name}/" \
            && ssh "${remote_user}@${host}" "sudo tar -xzf /tmp/${file} -C /data/web_static/releases/${name}/" \
            && ssh "${remote_user}@${host}" "sudo rm /tmp/${file}" \
            && ssh "${remote_user}@${host}" "sudo ln -sf /data/web_static/releases/${name}/ /data/web_static/current"

        # Validate the deployment
        ssh "${remote_user}@${host}" "[ -d /data/web_static/current ] && echo 'Validation Successful' || echo 'Validation Failed'"

        if [ $? -ne 0 ]; then
            return 1
        fi
    done
    return 0
}

function deploy {
    # Create and distribute an archive to a web server
    file=$(do_pack)
    if [ -z "${file}" ]; then
        return 1
    fi
    do_deploy "${file}"
}

deploy
