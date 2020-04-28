#!/bin/bash

printf "\nAtualizando repositórios...\n\n"
if ! apt-get update
then
    printf "\nNão foi possível atualizar os repositórios. Verifique seu arquivo /etc/apt/sources.list\n\n"
    exit 1
fi
printf "\nAtualização feita com sucesso\n\n"



printf "\nAtualizando pacotes já instalados\n\n"
if ! apt-get upgrade
then
    printf "\nNão foi possível atualizar pacotes.\n\n"
    exit 1
fi
printf "\nAtualização de pacotes feita com sucesso.\n\n"



printf "\nInstalando pacote Setup Tools.\n\n"
if ! apt-get install python-setuptools
then
    printf "\nNão foi possível instalar o pacote Setup Tools.\n\n"
    exit 1
fi
printf "\nPacote Setup Tools instalado com sucesso\n\n"



printf "\nInstalando pacote Pip.\n\n"
if ! easy_install pip
then
    printf "\nNão foi possível instalar o pacote Pip.\n\n"
    exit 1
fi
printf "\nPacote Pip instalado com sucesso\n\n"




printf "\nInstalando pacote Setup Tools 3\n\n"
if ! apt-get install python3-setuptools
then
    printf "\nNão foi possível instalar o pacote Setup Tools 3\n\n"
    exit 1
fi
printf "\nPacote Setup Tools 3 instalado com sucesso\n\n"



printf "\nInstalando pacote Pip3\n\n"
if ! easy_install3 pip
then
    printf "\nNão foi possível instalar o pacote Pip3.\n\n"
    exit 1
fi
printf "\nPacote Pip3 instalado com sucesso\n\n"



printf "\nInstalando pacote Python3 Pip.\n\n"
if ! apt-get install python3-pip
then
    printf "\nNão foi possível instalar o pacote Python3 Pip.\n\n"
    exit 1
fi
printf "\nPacote Python3 Pip instalado com sucesso”\n\n"



printf "\nInstalando pacote Wikipédia.\n\n"
if ! pip3 install wikipedia
then
    printf "\nNão foi possível instalar o pacote Wikipédia.\n\n"
    exit 1
fi
printf "\nPacote Wikipédia instalado com sucesso”\n\n"



printf "\nInstalndo pacote Speech Recgnition.\n\n"
if ! pip3 install --upgrade speechrecognition
then
    printf "\nNão foi possível instalar o pacote Speech Recgnition.\n\n"
    exit 1
fi
printf "\nPacote Speech Recgnition instalado com sucesso\n\n"



printf "\nInstalando pacote gTTS.\n\n"
if ! pip3 install gTTS
then
    printf "\nNão foi possível instalar o pacote gTTS.\n\n"
    exit 1
fi
printf "\nPacote gTTS instalado com sucesso.\n\n"



printf "\nInstalndo pacote Playsound.\n\n"
if ! pip3 install playsound
then
    printf "\nNão foi possível instalar o pacote Playsound.\n\n"
    exit 1
fi
printf "\nPacote Playsound instalado com sucesso\n\n"



printf "\nInstalando pacote Pyaudio.\n\n"
if ! apt install python3-pyaudio
then
    printf "\nNão foi possível instalar o pacote Pyaudio.\n\n"
    exit 1
fi
printf "\nPacote Pyaudio instalado com sucesso.\n\n"



printf "\nInstalando pacote lxml.\n\n"
if ! pip3 install lxml
then
    printf "\nNão foi possível instalar o pacote lxml.\n\n"
    exit 1
fi
printf "\nPacote lxml instalado com sucesso\n\n"








echo “Instalação finalizada”








