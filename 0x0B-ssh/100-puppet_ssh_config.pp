# configures a client ssh file to use no password and to use ~/.ssh/school private key
file { '~/.ssh/config':
  content =>'Host 54.198.80.67\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no'
}
