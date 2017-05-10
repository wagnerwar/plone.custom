====================
Exemplo de tematização do PLONE
====================

Plone é um sistema de gerenciamento de conteúdo (CMS, de Content Management System) escrito na linguagem Python e que roda sobre um Servidor de Aplicações Zope e sobre o framework CMF (Content Management Framework).

====================
Introdução
====================

Este plugin serve para demonstrar como se instala, via BUILDOUT, o PLONE, versão 4.3.3. Além disso, contém um exemplo prático de customização de leiaute do portal.

====================
Como instalar
====================
Neste plugin, foram feitos testes na distribuição CENTOS, versão 7. Caso você utilize uma distribuição diferente, reveja a síntaxe de alguns comandos apresentados aqui. 

Segue abaixo um exemplo de instalação

                          yum groupinstall 'Development Tools'
			  yum install nmap mod_ssl openssl openssl-devel zip unzip zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel libxml2-devel libxslt-devel python-setuptools wget
		          mkdir projetos
			  cd projetos

Baixar o projeto do git (plone.limpo)
                         git clone https://github.com/wagnerwar/plone.limpo.git
			 cd plone.limpo
			 wget https://raw.githubusercontent.com/buildout/buildout/master/bootstrap/bootstrap.py
			 python bootstrap.py
