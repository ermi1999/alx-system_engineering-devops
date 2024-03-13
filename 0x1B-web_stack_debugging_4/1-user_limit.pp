# updates a file limit for holberton.

exec {'update_the_hard_limit':
  command => 'sed -i "/^holberton hard nofile/ c\holberton hard nofile 30000" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin/', '/usr/local/bin/'],
}

exec {'update_the_soft_limit':
  command => 'sed -i "/^holberton soft nofile/ c\holberton soft nofile 10000" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin/', '/usr/local/bin/'],
}
