class Fligt:
    name_Airline        = ""
    name_Flight         = ""
    Coming              = ""
    Terminal            = ""
    Scheduled_Time      = ""
    Scheduled_Day       = ""
    Installation_Time   = ""
    Status              = ""

    def __init__(self, name_Airline,name_Flight,Coming,Terminal,Scheduled_Time,Scheduled_Day,Installation_Time,Status):
        self.name_Airline        = name_Airline
        self.name_Flight         = name_Flight
        self.Coming              = Coming
        self.Terminal            = Terminal
        self.Scheduled_Time      = Scheduled_Time
        self.Scheduled_Day       = Scheduled_Day
        self.Installation_Time   = Installation_Time
        self.Status              = Status

    def to_string(self):
        to_stg = {
                "name_Airline": self.name_Airline,
                "name_Flight": self.name_Flight,
                "Coming": self.Coming,
                "Terminal": self.Terminal,
                "Scheduled_Time": self.Scheduled_Time,
                "Scheduled_Day": self.Scheduled_Day,
                "Installation_Time": self.Installation_Time,
                "Status": self.Status
        }
        return to_stg

