import subprocess
import tqdm

# remove all lines in page_lines that contain a dead_link
# yeah this is n^2, idk if you can get any better.
def remove_dead_links(page_lines, dead_links):
	new_page_lines = []
	for line in page_lines:
		for link in dead_links:
			dead_link_flag = 0
			if link in line:
				dead_link_flag = 1
				break

		if not dead_link_flag:
			new_page_lines.append(line)

	return new_page_lines


def find_dead_yt_links(all_links):
	dead_links = []
	for i in tqdm.tqdm(range(len(all_links))):
		try:
			# simulate will just access the webpage. if the video dne anymore it will throw an error
			cmd_output = subprocess.check_output(['youtube-dl', '--simulate', all_links[i]], stderr=subprocess.DEVNULL);
		except subprocess.CalledProcessError as e:
			dead_links.append(all_links[i])
		# fyi the printing messes with tqdm formatting
		if (i % 50 == 0):
			print(f'Progress: {i} / {len(all_links)} - Found {len(dead_links)} dead links')
	
	return dead_links


if __name__ == '__main__':
	lines_in_page = []
	links = []
	with open('playlist.md', 'r') as page:
		lines_in_page = page.readlines()

	# this is pretty hard coded, the video link is at the end of the line
	# and the last two chars are ) and \n
	num_chars_in_yt_link = 45
	links = [x[-(num_chars_in_yt_link):-2] for x in lines_in_page if 'youtube.com' in x]
	dead_links = find_dead_yt_links(links)
	with open('dead_links.txt', 'w') as fp:
		for link in dead_links:
			fp.write(link + '\n')

	cleaned_page = remove_dead_links(lines_in_page, dead_links)

	with open('new_playlst.md', 'w') as fp:
		for line in cleaned_page:
			fp.write(line)

