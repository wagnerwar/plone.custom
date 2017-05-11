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

  yum groupinstall 'Development Tools'
  
  yum install nmap mod_ssl openssl openssl-devel zip unzip zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel libxml2-devel   libxslt-devel python-setuptools wget
  
  mkdir projetos
  
  cd projetos

Baixar o projeto do git (plone.limpo)

  git clone https://github.com/wagnerwar/plone.limpo.git
  
  cd plone.limpo
  
  wget https://raw.githubusercontent.com/buildout/buildout/master/bootstrap/bootstrap.py
  
  python bootstrap.py
  
Criação do arquivo sources.cfg (Configuração necessária para inclusão deste plugin na instalação)

  [buildout]
  
  extensions += mr.developer
  
  always-checkout = force
  
  auto-checkout =
  
      plone.custom
      
  [sources]
  
  plone.custom = git https://github.com/wagnerwar/plone.custom.git
  

Edição do arquivo buildout.cfg

Inclusão da referência do plugin na propriedade ‘extends’, para que o buildout consiga ler as configurações do arquivo recém-criado:

  extends =
  
     http://dist.plone.org/release/4.3.3/versions.cfg
  
     sources.cfg
  
Edição na diretivas eggs:

  eggs =
  
      Plone
      
      plone.app.upgrade
      
      plone.custom

Edição no arquivo setup.py (Inclusão da propriedade ‘install_requires’, dentro da função setup):

  setup(name='PloneClean',
    ...
  install_requires=[
    'plone.custom'
    ]
  )

bin/buildout -vvvc buildout.cfg

bin/instance fg

Caso tenha funcionado tudo bem, você pode testar abrindo seu navegador, e acessar o seguinte endereço: http://localhost:8080/. Por padrão, ele funciona na porta 8080.

Se estiver funcionando, você deverá ver algo conforme abaixo:

.. image:: img/imagem_a.png

Por padrão, são estes os dados de acesso:

  Username: admin
  Password: admin	
	
Aparecerá um formulário semelhante á este:

.. image:: img/imagem_b.png

Preencha os campos, e, no campo Complementos, selecione apenas o primeiro ítem: Tipos de conteúdo Dexterity

.. image:: img/imagem_c.png

Depois clique em Criar site Plone.

.. image:: img/imagem_d.png

Se tudo funcionar bem, aparecerá uma tela semelhante á esta:

.. image:: img/imagem_e.png

====================
Habilitar template personalizado
====================

Este plugin tem uma pasta chamada 'themes', que contém o tema personalizado. Porém, o mesmo, por padrão, não estará habilitado, estando apenas disponível para ser habilitado.

Para habilitá-lo, acesse o painel de configuração do site, conforme indicação abaixo, clicando em 'Configuração do Site':

.. image:: img/imagem_f.png

Em seguida, selecione Temas:

.. image:: img/imagem_j.png

Através de um mecanismo chamado Diazo, é possível, por exemplo, que você, com poucas linhas de código consiga refazer todo um leiaute do portal. 
O diazo permite que, de forma simplificada, você possa transformar um simples index.html no próprio leiaute padrão do portal. Para entender como funciona este mecanismo, vamos entender a estrutura de arquivos e diretórios do tema customizado do exemplo.
O Diazo tem suporte ao XSLT, que é uma espécie de linguagem de apresentação de documentos.

Caso queira analisar um exemplo de como funciona o XSLT, recomendo dar uma olhada no seguinte exemplo: https://github.com/wagnerwar/xsl.

Estrutura de diretórios e arquivos:
  assets/
  
  images/
  
  theme.html
  
  rules.xml
  
  preview.png
  
  manifest.cfg
































  





  


  

