import xml.etree.ElementTree as ET
import sys

# total arguments
n = len(sys.argv)

if n < 4:
   print("too few arguments. Exit")
   print("usage: ProgrammeName, FileSource, []files_names")
   sys.exit()





def change_in_file(filename):
   tree = ET.parse(filename)
   root = tree.getroot()

   for schedule_event in root.findall('ScheduledEvent'):
      for scheduled_element in schedule_event:
         event_data = scheduled_element.find('EventData')
            
         primary_event = event_data.find('PrimaryEvent')
         program_event = primary_event.find('ProgramEvent')
         program_name = program_event.find('ProgramName')
            # print("program name: ", program_name.tag, program_name.text)
            
         private_information = event_data.find('PrivateInformation')
         library_item = private_information.find('LibraryItem')
         file_source = library_item.find('FileSource')
            
         if program_name.text == sys.argv[1]:
            file_source.text = sys.argv[2]
            # file_source.set('updated', 'yes')
   
   tree.write('mod_'+filename)


change_in_file(sys.argv[3])
