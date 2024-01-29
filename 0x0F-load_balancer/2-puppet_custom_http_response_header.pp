# setup a nginx to ubuntu server.
exec {'update':
  command  => 'apt-get -y update',
  provider => 'shell'
}

package {'nginx':
  ensure  => present,
  require => Exec['update']
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx']
}

exec {'redirect':
  command  => 'sed -i "24c\        location /redirect_me { return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package[nginx]
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}

exec {'modify_header':
  command   => 'sed -i "12c\        add_header X-Served-By \'$hostname\';" /etc/nginx/nginx.conf'
  provider  => 'shell'
  require   => Package[nginx]
}
