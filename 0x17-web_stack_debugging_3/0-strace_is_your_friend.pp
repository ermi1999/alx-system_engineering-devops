# this program replaces all phpp ocurances with php to fix type error.

exec {'replace_phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin/', '/usr/local/bin/'],
}
