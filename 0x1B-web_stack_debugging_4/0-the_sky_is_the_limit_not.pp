# updates a file limit in nginx
exec { 'update_the_limit':
  command  => 'sudo sed -i \'s/15/30000/\' /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
