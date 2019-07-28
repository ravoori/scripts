show_highest_n()
{
	n=${1:?"Set number of elements to bubble"}
	shift
	sort_command_line=("$@")
	</dev/null sort "${sort_command_line[@]}" >/dev/null
	ret_code=$?
	if (( ret_code ))
	then
		printf 'Bad sort incantation!! %s\n' "${sort_command_line[*]}" >&2
		return $ret_code
	fi
	while IFS= read -r row
	do
		mapfile -t rows< <(printf "%s\n" "$row" ${not_first_row+"${rows[@]}"} | sort "${sort_command_line[@]}" | head -n "$n")
		not_first_row=1
		printf "\x1b[2J\x1b[H"; #clear screen, reposition cursor at left-top
		printf "%s\n" "${rows[@]}" #print sorted rows
	done	
}
