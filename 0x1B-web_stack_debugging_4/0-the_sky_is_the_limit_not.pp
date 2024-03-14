# updates a file limit in nginx
exec { 'limit':
  command => 'sed -i "/^ULIMIT=\\\"/ c\\ULIMIT=\\\"-n 2000\\\"" /etc/default/nginx',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
exec { 'restart':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin/', '/usr/local/bin/'],
}
