from datetime import datetime
from .models import Ligne,Planning
from .serializers import LigneSerializer
def calculate_all_hours(ligne):
    def parse_time(time_str):
        """Convert time string to datetime.time object"""
        if time_str:
            return datetime.strptime(time_str, "%H:%M:%S").time()  # Adjust format if needed
        return None

    # Convert string times to datetime.time
    start_hour = parse_time(ligne["start_hour"])
    end_hour = parse_time(ligne["end_hour"])
    start_cutoff = None
    end_cutoff = None
    if "end_cutoff" in  ligne and "start_cutoff"  in ligne:
      start_cutoff = parse_time(ligne["start_cutoff"]) if ligne["start_cutoff"] else None
      end_cutoff = parse_time(ligne["end_cutoff"]) if ligne["end_cutoff"] else None
    hours = 0

    # Function to calculate time difference in hours
    def time_difference_in_hours(start, end):
        start_time = datetime.combine(datetime.today(), start)
        end_time = datetime.combine(datetime.today(), end)
        diff =abs( end_time - start_time)
        return diff.total_seconds() / 3600  # Convert seconds to hours

    # Calculate the total hours
    if start_cutoff and end_cutoff:  
        hours = time_difference_in_hours(end_cutoff, end_hour) + time_difference_in_hours(start_hour, start_cutoff)
    else:
        hours = time_difference_in_hours(start_hour, end_hour)
    print("******1**\n")
    print(hours)
    if ligne.get("isPausePaid")== False:
        hours -= ligne["pause"]/60
        print("******2**\n")

        print(hours)
    hours = hours*ligne["month_days"].count("y")
    print("******3**\n")

    print(hours)

    return hours
def calculate_volume_horaire(planning):
 lignes = Ligne.objects.filter(planning=planning)
 lignes = LigneSerializer(lignes, many=True).data
 min_start_hour = None
 for ligne in lignes:
    ligne_start_hour = ligne["start_date"]
    if min_start_hour is None or ligne_start_hour < min_start_hour:
        min_start_hour = ligne_start_hour
     

 print(min_start_hour)
 return  {"volume_horaire": sum(  calculate_all_hours(ligne)*ligne["agent_number"] for ligne in lignes),
          "start_hour": min_start_hour
 }
 
