import re
import os
os.system('cls' if os.name == 'nt' else 'clear')


x = "https://www.helloworld23232.com"

pattern = r"https://www\.|\.com"
clean = re.sub(pattern,"",x)


def find_gov_urls(website):
 pattern = r"https?://[^\s,]+" #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []