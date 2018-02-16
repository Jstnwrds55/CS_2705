import ipaddress

# get list of ip addresses based on initial address block
ipInterface = ipaddress.ip_interface('138.191.0.0/16')
ipNetwork = ipInterface.network
collegeIP = (list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=4)))

# create list of colleges
colleges = ["Applied Science", "Arts & Humanities", "Education", "Business & Economics", "Health", "Science",
            "Social & Behavioral Science", "Information Technology", "Student Affairs", "Facilities Management",
            "Administrative Services"]
# create list of sub-colleges using multi-dimensional array
subColleges = [["Computer Science", "Professional Sales", "Manufacturing Engineering", "Construction Management",
               "Automotive Technology", "Network Technology", "Web Design", "Engineering"],
               ["Korean", "German", "Spanish", "French", "English", "Visual Arts", "Performing Arts", "Communications"],
               ["Child & Family Studies", "Health Promotion", "Athletic Training", "Human Performance",
                "Teacher Education", "Exercise Physiology", "Health Education", "Recreation Management"],
               ["Business Administration", "Economics", "Information Systems Tech", "Master of Business Admin",
                "Accounting", "Business Education", "Master of Accountancy", "Master of Taxation"],
               ["Dental Hygiene", "Emergency Care", "Health Information Management", "Nursing", "Medical Laboratory",
                "Radiology", "Respiratory Therapy", "Occupational Therapy"],
               ["Botany", "Geo-sciences", "Microbiology", "Developmental Math", "Physics", "Zoology", "Mathematics",
                "Human Anatomy Physiology"],
               ["Criminal Justice", "Geography", "History", "Military Science", "Philosophy & Poli Sci", "Psychology",
                "Social Work", "Sociology & Anthropology"],
               ["Computing Support", "Telecommunications", "Administrative Computing", "Networking",
                "Academic Computing", "Computer Security", "Database Administration", "VP of IT Office"],
               ["Student Life", "Student Services", "Outreach", "Academic Support", "Focused Interest",
                "Career Services", "Veterans Affairs", "Diversity"],
               ["Campus Planning", "Construction", "Custodial", "Landscaping", "Electrical", "Mechanical",
                "Business Services", "Parking Services"],
               ["Athletics", "Accounting", "Budget", "Environment Health & Safety", "Printing", "Human Resources",
                "Purchasing", "Police & Security"]]

# create string list of college ip addresses
collegeIPList = []
for x in range(0, len(collegeIP) - 1):
    collegeIPList.append(str(collegeIP[x]))

# print table for colleges
print("{: <26} {: >20} {: >37}".format("Name", "Network Address & Subnet", "Host IP Address Range"))
print('---------------------------------------------------------------------------------------------')
for x in range(0, len(colleges)):
    print("{: <30} {: >20} {: >20} - {}".format(colleges[x], collegeIPList[x], str(collegeIP[x].network_address + 1),
                                                str(collegeIP[x].broadcast_address - 1)))
print('\n')

# print table for each sub college
for x in range(0, len(colleges)):
    print("{: <26} {: >20} {: >37}".format(colleges[x], "Network Address & Subnet", "Host IP Address Range"))
    print('---------------------------------------------------------------------------------------------')

    # create ip addresses
    subIPInterface = ipaddress.ip_interface(collegeIPList[x])
    subIPNetwork = subIPInterface.network
    subCollegeIP = (list(ipaddress.ip_network(subIPNetwork).subnets(prefixlen_diff=3)))

    # create string list of sub college ip addresses for current college
    subCollegeIPList = []
    for i in range(0, len(subCollegeIP)):
        subCollegeIPList.append(str(subCollegeIP[i]))

    # print table information for current college's sub college
    for y in range(0, len(subColleges[x])):
        print("{: <30} {: >20} {: >20} - {}".format(subColleges[x][y], subCollegeIPList[y],
                                                    str(subCollegeIP[y].network_address + 1),
                                                    str(subCollegeIP[y].broadcast_address - 1)))

    print('\n')



