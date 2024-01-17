# puppet manuscript to replace a line of a file on a server

$filr_to_edit = '/var/www/html/wp-settings.php'

#replace line

exec { 'replace_line' : 
	command => "sed -i 's/phpp/php/g' $(file_to_edit)",
	path	=> ['/bin'', '/usr/bin']
}
