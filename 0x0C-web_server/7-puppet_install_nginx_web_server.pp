# setup a nginx to ubuntu server.

package {'update':
  ensure   => latest,
  provider => 'apt'
}

package {'nginx':
  ensure   => present
  provider => 'apt'
}

exec {"ufw allow 'Nginx HTTP'":
  provider  => 'shell'
}

file {"/var/www/html/index.nginx-debian.html":
  content => "Hello World!"
}

exec {"service nginx restart":
  provider => 'shell'
}
