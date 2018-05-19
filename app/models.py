# prajal mishra 1001434611
from app import DB

class Guest(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'guests'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    email = DB.Column(DB.String(120))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

class ZipCode(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'zipcodes_temp'
    zip_id = DB.Column(DB.String(100),primary_key=True)
    state = DB.Column(DB.String(100))
    county= DB.Column(DB.String(100))
    city= DB.Column(DB.String(100))


    def __init__(self, zip_id=None, state=None, county=None, city=None):
        self.zip_id = zip_id
        self.state = state
        self.county = county
        self.city = city


class education(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'education'
    unitid = DB.Column(DB.String(100),primary_key=True)
    opeid = DB.Column(DB.String(100))
    opeid6= DB.Column(DB.String(100))
    instnm= DB.Column(DB.String(100))
    city= DB.Column(DB.String(100))
    state= DB.Column(DB.String(100))
    insturl= DB.Column(DB.String(100))
    sat_avg= DB.Column(DB.String(100))
    graddebt= DB.Column(DB.String(100))


    def __init__(self, unitid=None, opeid=None, opeid6=None, instnm=None, city=None, state=None, insturl=None, sat_avg=None, graddebt=None):
        self.unitid = unitid
        self.opeid = opeid
        self.opeid6 = opeid6
        self.instnm = instnm
        self.city = city
        self.state = state
        self.insturl = insturl
        self.sat_avg = sat_avg
        self.graddebt = graddebt


class statevoting(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'statevoting'
    statename = DB.Column(DB.String(100),primary_key=True)
    totalpop = DB.Column(DB.String(100))
    votepop = DB.Column(DB.String(100))
    registered = DB.Column(DB.String(100))
    percentreg = DB.Column(DB.String(100))
    voted = DB.Column(DB.String(100))
    percentvote = DB.Column(DB.String(100))


    def __init__(self, statename=None, totalpop=None, votepop=None, registered=None, percentreg=None, voted=None, percentvote=None):
        self.statename = statename
        self.totalpop = totalpop
        self.votepop = votepop
        self.registered = registered
        self.percentreg = percentreg
        self.voted = voted
        self.percentvote = percentvote
        
class starbucks(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'starbucks'
    id1 = DB.Column(DB.String(100),primary_key=True)
    starbucksid = DB.Column(DB.String(100))
    name = DB.Column(DB.String(100))
    storenumber = DB.Column(DB.String(100))
    phonenumber = DB.Column(DB.String(100))
    street1 = DB.Column(DB.String(100))
    street2 = DB.Column(DB.String(100))
    street3 = DB.Column(DB.String(100))
    citybucks = DB.Column(DB.String(100))
    countrysubdivisioncode = DB.Column(DB.String(100))
    countrycode = DB.Column(DB.String(100))
    postalcode = DB.Column(DB.String(100))
    longitude = DB.Column(DB.String(100))
    latitude = DB.Column(DB.String(100))
    timezone = DB.Column(DB.String(100))


    def __init__(self, id1=None, starbucksid=None, name=None, storenumber=None, phonenumber=None, street1=None, street2=None, street3=None, citybucks=None, countrysubdivisioncode=None, countrycode=None, postalcode=None, longitude=None, latitude=None, timezone=None):
        self.id1 = id1
        self.starbucksid = starbucksid
        self.name = name
        self.storenumber = storenumber
        self.phonenumber = phonenumber
        self.street1 = street1
        self.street2 = street2
        self.street3 = street3
        self.citybucks = citybucks
        self.countrysubdivisioncode = countrysubdivisioncode
        self.countrycode = countrycode
        self.postalcode = postalcode
        self.longitude = longitude
        self.latitude = latitude
        self.timezone = timezone


class students(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'students'
    givenname = DB.Column(DB.String(100),primary_key=True)
    surname = DB.Column(DB.String(100))
    address = DB.Column(DB.String(100))
    city = DB.Column(DB.String(100))
    state = DB.Column(DB.String(100))
    statefull = DB.Column(DB.String(100))
    zipcode = DB.Column(DB.String(100))
    email = DB.Column(DB.String(100))
    username = DB.Column(DB.String(100))
    password = DB.Column(DB.String(100))
    telephone = DB.Column(DB.String(100))
    mothermaiden = DB.Column(DB.String(100))
    birthday = DB.Column(DB.String(100))
    age = DB.Column(DB.String(100))
    ccnum = DB.Column(DB.String(100))
    cvv2 = DB.Column(DB.String(100))
    nationalid = DB.Column(DB.String(100))
    bloodtype = DB.Column(DB.String(100))
    kilograms = DB.Column(DB.String(100))
    centimeters = DB.Column(DB.String(100))
    latitude = DB.Column(DB.String(100))
    longitude = DB.Column(DB.String(100))

    def __init__(self, givenname=None, surname=None, address=None, city=None, state=None, statefull=None, 
        zipcode=None, email=None, username=None, password=None, telephone=None, mothermaiden=None, birthday=None, 
        age=None, ccnum=None, cvv2=None, nationalid=None, bloodtype=None, kilograms=None, centimeters=None, latitude=None, longitude=None):

        self.givenname = givenname
        self.surname = surname
        self.address = address
        self.city = city
        self.state = state
        self.statefull = statefull
        self.zipcode = zipcode
        self.email = email
        self.username = username
        self.password = password
        self.telephone = telephone
        self.mothermaiden = mothermaiden
        self.birthday = birthday
        self.age = age
        self.ccnum = ccnum
        self.cvv2 = cvv2
        self.nationalid = nationalid
        self.bloodtype = bloodtype
        self.kilograms = kilograms
        self.centimeters = centimeters
        self.latitude = latitude
        self.longitude = longitude

class classes(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'classes'
    course = DB.Column(DB.String(100))
    section = DB.Column(DB.String(100))
    instructor = DB.Column(DB.String(100),primary_key=True)
    room = DB.Column(DB.String(100))    

    def __init__(self, course=None, section=None, instructor=None, room=None):
        self.course = course
        self.section = section
        self.instructor = instructor
        self.room = room
        
class csefall2018(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'csefall2018'
    subject = DB.Column(DB.String(100))
    coursenum = DB.Column(DB.String(100),primary_key=True)
    sectionnum = DB.Column(DB.String(100))
    classnum = DB.Column(DB.String(100))
    mon = DB.Column(DB.String(100))
    tue = DB.Column(DB.String(100))
    wed = DB.Column(DB.String(100))
    thur = DB.Column(DB.String(100))
    fri = DB.Column(DB.String(100))
    sat = DB.Column(DB.String(100))
    sun = DB.Column(DB.String(100))
    approval = DB.Column(DB.String(100))
    maxenroll = DB.Column(DB.String(100))
    

    def __init__(self, subject=None, coursenum=None, sectionnum=None, classnum=None, mon=None, tue=None, wed=None, thur=None, fri=None, sat=None, sun=None, approval=None, maxenroll=None):
        self.subject = subject
        self.coursenum = coursenum
        self.sectionnum = sectionnum
        self.classnum = classnum
        self.mon = mon
        self.tue = tue
        self.wed = wed
        self.thur = thur
        self.fri = fri
        self.sat = sat
        self.sun = sun
        self.approval = approval
        self.maxenroll = maxenroll
        