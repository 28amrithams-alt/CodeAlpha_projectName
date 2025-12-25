# data.py

DATASET = [
    {
        "id": 1,
        "category": "medical_emergency",
        "patterns": [
            "Someone fainted",
            "A person fainted",
            "Person unconscious",
            "Man collapsed",
            "Woman collapsed",
            "Someone fell down unconscious",
            "He is not responding",
            "She is not responding"
        ],
        "response": "Stay calm. Check if the person is breathing. Call the medical emergency helpline immediately and ask nearby people for help. Do not give food or water and do not move the person unless there is danger nearby."
    },

    {
        "id": 2,
        "category": "ambulance",
        "patterns": [
            "How to call an ambulance",
            "Ambulance number",
            "Need ambulance",
            "Call ambulance",
            "Emergency ambulance",
            "Ambulance help"
        ],
        "response": "To call an ambulance, use the official medical emergency helpline number for your region. Provide clear details of the location, what happened, and the condition of the person."
    },

# ---------------------------
# EMERGENCY PUBLIC CHATBOT DATASET (~200+ patterns)
# ---------------------------


   
    {
        "id": 3,
        "category": "bleeding",
        "patterns": [
            "A person is bleeding",
            "He is bleeding badly",
            "She is bleeding",
            "Too much blood",
            "How to stop bleeding"
        ],
        "response": "If it is safe, apply gentle but firm pressure on the wound using clean cloth or tissue. Ask someone to call medical emergency immediately. Do not remove any deeply stuck object from the wound and do not give the person anything to eat or drink."
    },
    {
        "id": 4,
        "category": "heart_attack_suspicion",
        "patterns": [
            "Heart attack",
            "Chest pain emergency",
            "He has chest pain",
            "She has chest pain",
            "Serious chest pain",
            "Heart problem right now"
        ],
        "response": "If someone has sudden chest pain, difficulty breathing, sweating, or pain spreading to arm, jaw or back, treat it as an emergency. Call the medical emergency helpline immediately and let the person rest in a comfortable sitting position. Do not let them walk around."
    },
    {
        "id": 5,
        "category": "breathing_problem",
        "patterns": [
            "He cannot breathe",
            "She cannot breathe",
            "Breathing problem",
            "Breathing difficulty",
            "Short of breath",
            "Struggling to breathe"
        ],
        "response": "This is an emergency. Call the medical emergency helpline immediately. Help the person sit upright, loosen tight clothing, and encourage slow, relaxed breathing if possible. Do not force them to lie down unless they feel faint."
    },
    {
        "id": 6,
        "category": "burns",
        "patterns": [
            "He got burned",
            "She got burned",
            "Fire burn injury",
            "Skin burn",
            "Hot water burn"
        ],
        "response": "If the burn is from heat, cool the area gently with room temperature or slightly cool running water for several minutes. Do not apply ice, toothpaste, oil, or any home remedy. Cover the area loosely with a clean cloth and seek medical help for serious burns."
    },
    {
        "id": 7,
        "category": "seizure",
        "patterns": [
            "He is having fits",
            "She is having fits",
            "Seizure",
            "Epileptic attack",
            "Body shaking suddenly"
        ],
        "response": "Do not hold the person down and do not put anything in their mouth. Move nearby objects away to prevent injury. Place something soft under their head if possible. Once the shaking stops, turn them gently onto one side. Call the medical emergency helpline if it is their first seizure or if it lasts more than a few minutes."
    },
    {
        "id": 8,
        "category": "poisoning",
        "patterns": [
            "He drank poison",
            "She drank poison",
            "Poisoned",
            "Chemical ingestion",
            "Swallowed tablets",
            "Overdose"
        ],
        "response": "This is a serious emergency. Call the medical emergency helpline immediately. Do not force the person to vomit unless a medical professional specifically tells you to do so. If possible, keep the container or medicine strip to show to the doctors."
    },
    {
        "id": 9,
        "category": "stroke_suspicion",
        "patterns": [
            "Face bending on one side",
            "He cannot move one side",
            "She cannot move hand and leg",
            "Stroke symptoms",
            "Sudden weakness one side"
        ],
        "response": "This may be a stroke. Watch for face drooping, arm weakness, and difficulty speaking. Call the medical emergency helpline immediately. Time is critical, do not delay. Help the person sit or lie in a safe and comfortable position until help arrives."
    },
    {
        "id": 10,
        "category": "general_medical_help",
        "patterns": [
            "General medical help",
            "Medical emergency help",
            "What to do in medical emergency",
            "Serious health problem",
            "Help in medical issue"
        ],
        "response": "In any serious medical emergency, stay calm and call the official medical emergency helpline for your region. Provide clear location details, describe what happened, and follow the instructions given by the operator. Try to keep the person comfortable and safe until help arrives."
    },

    # 11–20: Nearest hospital / clinic
    {
        "id": 11,
        "category": "nearest_hospital",
        "patterns": [
            "Where is the nearest hospital",
            "Nearest hospital location",
            "Hospital nearby",
            "Any hospital near this place",
            "How to go to hospital from here"
        ],
        "response": "The nearest hospital information should be configured based on this chatbot's location. Typically, guide the user to the closest major hospital or emergency care center and provide directions if available."
    },
    {
        "id": 12,
        "category": "nearest_clinic",
        "patterns": [
            "Nearest clinic",
            "Small clinic nearby",
            "Doctor clinic near bus stand",
            "Any clinic close to here"
        ],
        "response": "Please visit the nearest registered clinic or hospital for non‑life‑threatening issues. This system should be configured with local clinic addresses based on the exact location where the chatbot is installed."
    },

    # 21–30: Accidents & police
    {
        "id": 21,
        "category": "road_accident",
        "patterns": [
            "There is a road accident",
            "Accident happened here",
            "Bus accident",
            "Bike accident",
            "Car crash",
            "Auto accident"
        ],
        "response": "Ensure your own safety first. If possible, call the local police helpline and the medical emergency helpline. Give the exact location, number of injured people, and type of accident. Do not crowd the area or move injured persons unless there is immediate danger."
    },
    {
        "id": 22,
        "category": "how_to_report_accident",
        "patterns": [
            "How to report an accident",
            "How to complain about road accident",
            "What to do after accident here"
        ],
        "response": "Call the official police helpline for your region and explain clearly that an accident has occurred. Share location, number of vehicles involved, and number of injured people if known. Stay nearby at a safe distance to guide responders if needed."
    },
    {
        "id": 23,
        "category": "police_station_location",
        "patterns": [
            "Where is the police station",
            "Nearest police station",
            "Police station nearby",
            "How to reach police station"
        ],
        "response": "The nearest police station address should be configured according to this chatbot's installation location. Normally, you can also call the police helpline for urgent help instead of visiting directly."
    },
    {
        "id": 24,
        "category": "police_helpline",
        "patterns": [
            "Police helpline number",
            "How to call police",
            "Emergency police number",
            "Call police"
        ],
        "response": "Use the official police emergency helpline for your country or region. When you call, speak clearly, mention the exact place, what is happening, and if anyone is in danger. Stay on the line until they have enough details."
    },

    # 31–40: Fire and hazards
    {
        "id": 31,
        "category": "fire_emergency",
        "patterns": [
            "There is a fire",
            "Fire in bus stand",
            "Fire in railway station",
            "Shop is burning",
            "Building on fire"
        ],
        "response": "Move away from the fire to a safe open area. Activate any nearby fire alarm if available and call the fire emergency helpline. Do not use lifts and do not run into smoke. Follow official staff instructions if present."
    },
    {
        "id": 32,
        "category": "gas_leak",
        "patterns": [
            "Gas leak smell",
            "I smell gas",
            "Gas leakage",
            "Strong gas odour"
        ],
        "response": "Do not use matches, lighters, or electrical switches. Move to an open, ventilated area immediately and alert others calmly. Inform the authorities or fire emergency helpline about the suspected gas leak and follow their instructions."
    },
    {
        "id": 33,
        "category": "fire_extinguisher",
        "patterns": [
            "Where is the fire extinguisher",
            "Fire extinguisher location",
            "How to use fire extinguisher"
        ],
        "response": "Fire extinguishers are usually placed near exits, staircases, and critical points. Only use a fire extinguisher if the fire is small and you have been trained to use it. Otherwise, move to safety and wait for trained personnel."
    },
    {
        "id": 34,
        "category": "evacuation_route",
        "patterns": [
            "How to evacuate",
            "Evacuation route",
            "Exit route in emergency",
            "How to go out safely"
        ],
        "response": "During emergencies, follow the marked exit signs and move calmly towards open and safe areas. Do not run, do not push others, and avoid using lifts. Help children, elderly people, and persons with disabilities if you can do so safely."
    },

    # 41–60: Lost items and missing people
    {
        "id": 41,
        "category": "lost_item",
        "patterns": [
            "I lost my bag",
            "My bag is missing",
            "Lost wallet",
            "Lost phone",
            "I cannot find my luggage",
            "My suitcase is missing"
        ],
        "response": "Stay calm and try to remember where you last had the item. Report the loss immediately to the nearest help desk, security office, or lost and found section if available. Share a clear description of the item and your contact details."
    },
    {
        "id": 42,
        "category": "lost_and_found_office",
        "patterns": [
            "Where is lost and found",
            "Lost and found counter location",
            "Lost and found office",
            "Where to report lost item"
        ],
        "response": "The lost and found counter is usually located near the main enquiry or security office in bus stands and railway stations. This system should be configured with the exact location for this particular place."
    },
    {
        "id": 43,
        "category": "missing_child",
        "patterns": [
            "My child is missing",
            "I lost my kid",
            "Child missing in station",
            "Child missing in bus stand"
        ],
        "response": "Inform security staff or the police immediately and describe the child’s age, clothes, and last known location. Do not leave the area completely; stay near a central point where the child might be brought if found. Request announcements if available."
    },
    {
        "id": 44,
        "category": "missing_person",
        "patterns": [
            "My friend is missing",
            "Family member missing",
            "Person missing in station",
            "Cannot find my relative"
        ],
        "response": "Report the missing person to security or police with their name, age, clothing, and last known location. Check common waiting areas, platforms, and information counters. Give your contact details so they can reach you if the person is found."
    },

    # 61–90: Travel confusion, bus stand, railway station help
    {
        "id": 61,
        "category": "platform_information",
        "patterns": [
            "Which platform for my train",
            "Where is platform 1",
            "Platform number for this train",
            "Train platform help"
        ],
        "response": "Platform numbers can change. Please check the nearest electronic display board or enquiry counter for the latest platform information. Follow the signs carefully to reach the correct platform safely."
    },
    {
        "id": 62,
        "category": "missed_train",
        "patterns": [
            "I missed my train",
            "Train already left what to do",
            "My train departed",
            "Missed train help"
        ],
        "response": "If you missed your train, visit the railway enquiry counter or ticket counter for guidance on refund rules or alternate trains. Keep your ticket and any booking details with you when you ask for help."
    },
    {
        "id": 63,
        "category": "bus_enquiry",
        "patterns": [
            "Which bus should I take",
            "Bus to city center",
            "Bus to airport",
            "How to go to town by bus"
        ],
        "response": "Please check the route boards or bus enquiry counter for the correct bus number and platform. Ask staff or drivers if you are unsure before boarding the bus."
    },
    {
        "id": 64,
        "category": "missed_bus",
        "patterns": [
            "I missed my bus",
            "Bus already left",
            "My bus went what to do"
        ],
        "response": "Check if there is another bus on the same route soon. Visit the enquiry counter or ticket counter for updated schedules and options. Keep your ticket or booking details while asking for help."
    },
    {
        "id": 65,
        "category": "ticket_counter_location",
        "patterns": [
            "Where is the ticket counter",
            "Ticket booking counter location",
            "Where to buy ticket",
            "Ticket office"
        ],
        "response": "Ticket counters are usually located near the main entrance or central hall. Follow the signboards marked as 'Ticket Counter' or 'Reservation' for this station or bus stand."
    },
    {
        "id": 66,
        "category": "online_ticket_help",
        "patterns": [
            "I booked ticket online",
            "Online ticket problem",
            "Ticket not showing in phone",
            "Online booking issue"
        ],
        "response": "For online booking issues, contact the official customer support of the booking app or website you used. At the station or bus stand, you can show your booking ID, SMS, or email at the enquiry counter for basic assistance."
    },
    {
        "id": 67,
        "category": "safety_on_platform",
        "patterns": [
            "Is it safe to stand near tracks",
            "Platform safety",
            "How to stay safe on platform",
            "Safety rules for railway station"
        ],
        "response": "Always stand behind the safety line on the platform and stay away from the edge. Do not cross railway tracks; use only bridges or subways. Avoid running, pushing, or using headphones loudly near trains."
    },
    {
        "id": 68,
        "category": "general_travel_safety",
        "patterns": [
            "How to stay safe while travelling",
            "General safety tips for bus stand",
            "Safety in railway station",
            "Travel safety advice"
        ],
        "response": "Keep your belongings close, avoid displaying large amounts of cash, and stay in well‑lit, crowded areas. Do not share personal details with strangers. In case of any trouble, contact security staff or the police."
    },

    # 91–120: Women’s safety and harassment
    {
        "id": 91,
        "category": "harassment_report",
        "patterns": [
            "Someone is harassing me",
            "A man is disturbing me",
            "Person misbehaving with me",
            "I am being harassed here"
        ],
        "response": "Your safety is important. Move towards a crowded, well‑lit area or near families. Inform security staff, police, or women’s help center as soon as possible. If you can, call the women’s helpline or police emergency number."
    },
    {
        "id": 92,
        "category": "feeling_unsafe",
        "patterns": [
            "I feel unsafe here",
            "This place is scary",
            "I do not feel safe",
            "I am scared here"
        ],
        "response": "If you feel unsafe, move closer to well‑lit and crowded areas like ticket counters, waiting halls, or shops. Stand near families or groups and try to stay visible. If the feeling continues, contact security staff or call the emergency helpline."
    },
    {
        "id": 93,
        "category": "women_helpline",
        "patterns": [
            "Women helpline number",
            "How to contact women helpline",
            "Women safety number"
        ],
        "response": "Use the official women’s helpline number for your region if you feel threatened or harassed. You can also contact the police emergency helpline or approach nearby security staff immediately."
    },
    {
        "id": 94,
        "category": "safe_waiting_area",
        "patterns": [
            "Where is safe waiting area",
            "Safe place to wait",
            "Where can I wait safely"
        ],
        "response": "Safe waiting areas are usually near main halls, ticket counters, or designated waiting rooms with lighting and CCTV. This chatbot system should be configured with the exact safe zones for this location."
    },

    # 121–150: Weather, natural issues, local info
    {
        "id": 121,
        "category": "heavy_rain",
        "patterns": [
            "Heavy rain what to do",
            "It is raining heavily",
            "Flood like situation here",
            "Road full of water"
        ],
        "response": "Avoid walking through deep or fast‑moving water. Stay on higher ground and use covered walkways if available. Check official weather or traffic updates for warnings before travelling further."
    },
    {
        "id": 122,
        "category": "flood_warning",
        "patterns": [
            "Is there flood warning",
            "Flood alert now",
            "Is it safe to travel in rain"
        ],
        "response": "Check official weather and disaster management updates for accurate flood alerts. If there is a warning, avoid unnecessary travel and move to higher and safer locations as guided by authorities."
    },

    # 151–180: Basic amenities and help
    {
        "id": 151,
        "category": "drinking_water",
        "patterns": [
            "Where is drinking water",
            "Drinking water point",
            "Water purifier location",
            "Place to drink water"
        ],
        "response": "Drinking water points are usually located near waiting halls, restrooms, or food stalls. Follow the signboards for 'Drinking Water'. This system should be updated with exact spots for this place."
    },
    {
        "id": 152,
        "category": "restroom_location",
        "patterns": [
            "Where is the toilet",
            "Restroom location",
            "Bathroom near me",
            "Washroom in bus stand",
            "Washroom in railway station"
        ],
        "response": "Restrooms are usually near the main waiting area or along corridors with clear signs indicating 'Toilet' or 'Restroom'. Follow the direction boards or ask nearby staff if you are unsure."
    },
    {
        "id": 153,
        "category": "mobile_charging",
        "patterns": [
            "Where can I charge my phone",
            "Mobile charging point",
            "Charging station location",
            "Phone charging facility"
        ],
        "response": "Mobile charging points are often provided near waiting areas or designated charging zones. Look for signs mentioning 'Charging Point' or ask at the enquiry counter for the nearest location."
    },
    {
        "id": 154,
        "category": "wifi_availability",
        "patterns": [
            "Is WiFi available here",
            "Free WiFi here",
            "How to use WiFi in station",
            "WiFi facility"
        ],
        "response": "Some bus stands and railway stations provide public WiFi. Check for signboards with network name and instructions or ask at the enquiry counter. Use public WiFi carefully and avoid accessing sensitive accounts."
    },
    {
        "id": 155,
        "category": "cctv_presence",
        "patterns": [
            "Is there CCTV here",
            "CCTV cameras in this place",
            "Is area under surveillance"
        ],
        "response": "Many public places, bus stands, and stations use CCTV for security. For exact information, check signboards or ask security staff. Still, keep your belongings safe and stay aware of your surroundings."
    },
    {
        "id": 156,
        "category": "security_office",
        "patterns": [
            "Where is security office",
            "Security guard room location",
            "Security cabin",
            "Where can I find security staff"
        ],
        "response": "Security offices are usually near main entrances, platforms, or central halls. This system should be configured with the exact security office location for this station or bus stand."
    },

    # 181–200: Language, technical help, general guidance
    {
        "id": 181,
        "category": "change_language",
        "patterns": [
            "Change language",
            "Can you speak Malayalam",
            "Can you speak Hindi",
            "Change to English",
            "I want another language"
        ],
        "response": "You can change the language using the options provided on the screen, if available. Choose your preferred language and then continue asking your question."
    },
    {
        "id": 182,
        "category": "how_to_use_chatbot",
        "patterns": [
            "How to use this machine",
            "How to use this chatbot",
            "What can you do",
            "How do I ask questions"
        ],
        "response": "You can type or speak simple questions like 'Where is the restroom', 'How to call ambulance', or 'Where is ticket counter'. I will try to guide you with basic, general information for this place."
    },
   

    # ⬇ PASTE ALL YOUR OTHER ENTRIES HERE ⬇
    # IDs 3 to 182 (fire, police, women safety, travel, facilities, etc.)

    {
        "id": 183,
        "category": "general_greeting",
        "patterns": ["Hello", "Hi", "Hey", "Good morning", "Good evening"],
        "response": "Hello. I am a public help chatbot. You can ask about emergencies, safety, directions, and facilities."
    },

    {
        "id": 184,
        "category": "goodbye",
        "patterns": ["Thank you", "Thanks", "Bye", "Okay done", "That is all"],
        "response": "You are welcome. Stay safe and have a good journey."
    }
]