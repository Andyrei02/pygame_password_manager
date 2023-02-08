import settings
import os

class WriteRead:
	def write(self):
		with open(os.path.join('passwords', f'{settings.Title}.txt'), 'a') as f:
			f.write('platform: ' + settings.Title + '\n')
			f.write('E-Mail Adresse: ' + settings.EMail + '\n')
			f.write('Username: ' + settings.UserName + '\n')
			f.write('Password: ' + settings.Password + '\n')

	def read(self, file):
		with open(os.path.join('passwords', file), 'r') as f:
			# r = f.read()
			list_line=[]
			for line in f:
				# r = line
				list_line.append(line)
				# print(line)
			return list_line
