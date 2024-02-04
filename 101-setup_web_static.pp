# Setup and deploy web static to nginx

class { 'nginx':
  ensure => installed,
}

firewall { 'Nginx HTTP':
  proto  => 'tcp',
  dport  => 80,
  action => 'accept',
}

file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  content => '<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
  </html>',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
}

file { '/data/':
  ensure => directory,
  recurse => true,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

nginx::resource::location { '/hbnb_static':
  alias => '/data/web_static/current/',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/data/web_static/current'],
}

