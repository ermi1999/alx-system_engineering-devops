# updates a file limit in nginx
exec { 'limit':
  command  => 'sudo sed -i "/^ULIMIT=\\\"/ c\\ULIMIT=\\\"-n 2000\\\"" /etc/default/nginx',
  provider => shell,
}
exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
