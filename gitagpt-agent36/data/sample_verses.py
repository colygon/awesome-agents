"""
Sample verses from the Bhagavad Gita for reference
Agent 36 - CrewAI Upgrade
"""

BHAGAVAD_GITA_VERSES = {
    "2.47": {
        "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन। मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥",
        "transliteration": "karmaṇy-evādhikāras te mā phaleṣhu kadāchana, mā karma-phala-hetur bhūr mā te saṅgo 'stvakarmaṇi",
        "translation": "You have a right to perform your prescribed duty, but you are not entitled to the fruits of action. Never consider yourself the cause of the results of your activities, and never be attached to not doing your duty.",
        "chapter": 2,
        "verse": 47,
        "theme": "Karma Yoga - Action without attachment to results"
    },
    "2.14": {
        "sanskrit": "मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदुःखदाः। आगमापायिनोऽनित्यास्तांस्तितिक्षस्व भारत॥",
        "transliteration": "mātrā-sparśhās tu kaunteya śhītoṣhṇa-sukha-duḥkha-dāḥ, āgamāpāyino 'nityās tans-titikṣhasva bhārata",
        "translation": "The contact between the senses and the sense objects gives rise to fleeting sensations of pleasure and pain. These are non-permanent, and come and go like the winter and summer seasons. Endure them with patience.",
        "chapter": 2,
        "verse": 14,
        "theme": "Equanimity - Enduring pleasure and pain"
    },
    "6.5": {
        "sanskrit": "उद्धरेदात्मनात्मानं नात्मानमवसादयेत्। आत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मनः॥",
        "transliteration": "uddhared ātmanātmānaṁ nātmānam avasādayet, ātmaiva hyātmano bandhur ātmaiva ripur ātmanaḥ",
        "translation": "Elevate yourself through the power of your mind, and not degrade yourself, for the mind can be the friend and also the enemy of the self.",
        "chapter": 6,
        "verse": 5,
        "theme": "Self-mastery - Mind as friend or foe"
    },
    "2.20": {
        "sanskrit": "न जायते म्रियते वा कदाचिन् नायं भूत्वा भविता वा न भूयः। अजो नित्यः शाश्वतोऽयं पुराणो न हन्यते हन्यमाने शरीरे॥",
        "transliteration": "na jāyate mriyate vā kadāchin nāyaṁ bhūtvā bhavitā vā na bhūyaḥ, ajo nityaḥ śhāśhvato 'yaṁ purāṇo na hanyate hanyamāne śharīre",
        "translation": "The soul is never born and never dies. It is unborn, eternal, ever-existing, and primeval. It is not slain when the body is slain.",
        "chapter": 2,
        "verse": 20,
        "theme": "Nature of the soul - Immortality"
    },
    "3.27": {
        "sanskrit": "प्रकृतेः क्रियमाणानि गुणैः कर्माणि सर्वशः। अहङ्कारविमूढात्मा कर्ताहमिति मन्यते॥",
        "transliteration": "prakṛiteḥ kriyamāṇāni guṇaiḥ karmāṇi sarvaśhaḥ, ahaṅkāra-vimūḍhātmā kartāham iti manyate",
        "translation": "All activities are carried out by the three modes of material nature. But in ignorance, the soul, deluded by false identification with the body, thinks itself to be the doer.",
        "chapter": 3,
        "verse": 27,
        "theme": "Understanding ego - False identification"
    },
    "18.66": {
        "sanskrit": "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज। अहं त्वां सर्वपापेभ्यो मोक्षयिष्यामि मा शुचः॥",
        "transliteration": "sarva-dharmān parityajya mām ekaṁ śharaṇaṁ vraja, ahaṁ tvāṁ sarva-pāpebhyo mokṣhayiṣhyāmi mā śhuchaḥ",
        "translation": "Abandon all varieties of dharma and simply surrender unto Me alone. I shall liberate you from all sinful reactions; do not fear.",
        "chapter": 18,
        "verse": 66,
        "theme": "Surrender - Ultimate teaching of the Gita"
    },
    "2.56": {
        "sanskrit": "दुःखेष्वनुद्विग्नमनाः सुखेषु विगतस्पृहः। वीतरागभयक्रोधः स्थितधीर्मुनिरुच्यते॥",
        "transliteration": "duḥkheṣhv-anudvigna-manāḥ sukheṣhu vigata-spṛihaḥ, vīta-rāga-bhaya-krodhaḥ sthita-dhīr munir uchyate",
        "translation": "One whose mind remains undisturbed amidst misery, who does not crave for pleasure, and who is free from attachment, fear, and anger, is called a sage of steady wisdom.",
        "chapter": 2,
        "verse": 56,
        "theme": "Steady wisdom - Characteristics of a sage"
    },
    "4.7": {
        "sanskrit": "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत। अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम्॥",
        "transliteration": "yadā yadā hi dharmasya glānir bhavati bhārata, abhyutthānam adharmasya tadātmānaṁ sṛijāmyaham",
        "translation": "Whenever there is a decline in righteousness and an increase in unrighteousness, O Arjuna, at that time I manifest myself on earth.",
        "chapter": 4,
        "verse": 7,
        "theme": "Divine incarnation - Protection of dharma"
    }
}


def get_verse_by_reference(chapter, verse):
    """Get a specific verse by chapter and verse number"""
    ref = f"{chapter}.{verse}"
    return BHAGAVAD_GITA_VERSES.get(ref)


def search_verses_by_theme(theme_keyword):
    """Search verses by theme keyword"""
    results = []
    for ref, verse_data in BHAGAVAD_GITA_VERSES.items():
        if theme_keyword.lower() in verse_data['theme'].lower():
            results.append((ref, verse_data))
    return results


def get_all_verses():
    """Get all verses in the collection"""
    return BHAGAVAD_GITA_VERSES
