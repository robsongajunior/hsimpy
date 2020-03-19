#!/bin/bash


function uninstall() {
    pip3 uninstall hsimp -y;
}

function pkg_install() {
    python3 setup.py bdist_wheel;
    python3 setup.py bdist_wheel;
    pip3 wheel --wheel-dir=dist requirements.txt;
}

function install_whl() {
    pip3 install dist/hsimp3-0.0.5-py3-none-any.whl;
}

function install() {
    pkg_install
    install_whl
}

function pep8() {
    pycodestyle ./hsimp3/*.py
}

function pylnt() {
    pylint ./hsimp3/*.py;
}

function lint() {
    pylnt
    pep8
}

function tests() {
    python3 -m unittest discover tests
}

function pipeline() {
    lint
    uninstall
    install
    tests
}

function clean_images() {
    docker rmi -f $(docker images | grep $2 | awk '{print $3}')
}

$1
