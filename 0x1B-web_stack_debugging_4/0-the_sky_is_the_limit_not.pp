# updates a file limit in nginx
exec { 'limit':
  command => 'echo "ULIMIT=\"-n 1096\"" > /etc/default/nginx',
  path    => ['/bin', '/usr/bin/', '/usr/local/bin/'],
}

exec { 'restart':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin/', '/usr/local/bin/'],
}
