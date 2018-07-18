{{cookiecutter.project_name}} 
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}

Setup do servidor de produção
-----------------------------

### Docker
```
sudo apt-get update

# https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-16-04-pt
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
sudo apt-get install -y docker-engine
sudo groupadd docker
sudo usermod -aG docker $USER
```

### Python 3
```
sudo apt-get install -y git python-pip make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev

sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod 0777 /usr/local/bin/docker-compose

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

exec "$SHELL"

pyenv install 3.6.1
pyenv virtualenv 3.6.1 api-receita


```

### Projeto

__Antes de tudo__: crie e insira no github uma chave de deployment)

```
cd
git clone git@github.com:moacirmoda/api-receita.git git
```

Copie e configure o `.env` do projeto
```
mkdir pgdata
cp env-sample .env

echo "CURRENT_UID=$(id -u):$(id -g)" >> .env
```



