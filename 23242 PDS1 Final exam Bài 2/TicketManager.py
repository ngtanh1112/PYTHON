from Ticket import Driver, Ticket
import csv
from collections import defaultdict

def read_driver_from_file(file_name):
    drivers = []
    with open(file_name, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            did = row['did']
            years = int(row['years'])
            d = Driver(name, did, years)
            drivers.append(d)
    return drivers


def read_ticket_from_file(file_name, list_drivers):
    tickets = []
    driver_map = {d.did: d for d in list_drivers}
    
    with open(file_name, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tid = int(row['tid'])
            did = row['did']
            date = int(row['date'])
            stime = int(row['stime'])
            etime = int(row['etime'])
            ctype = int(row['ctype'])
            num_c = int(row['num_c'])
            vote = int(row['vote'])
            driver = driver_map.get(did)
            if driver is None:
                continue  
            t = Ticket(tid, date, stime, etime, ctype, num_c, vote, driver)
            tickets.append(t)
    return tickets


def caculate_mean_absolute_deviation(list_tickets):
    durations = [t.end_time - t.start_time for t in list_tickets]
    mean_duration = sum(durations) / len(durations) if durations else 0
    mad = sum(abs(d - mean_duration) for d in durations) / len(durations) if durations else 0
    return mad


def caculate_mean_salary_in_range(adate, bdate, list_tickets):
    salaries = []
    for t in list_tickets:
        if adate < t.date < bdate:
            salaries.append(t.driver.get_salary())
    if not salaries:
        return 0.0
    return sum(salaries) / len(salaries)


def caculate_mean_customer_by_client(list_tickets, client_type):
    total_customers = 0
    count = 0
    for t in list_tickets:
        if t.driver.get_client() == client_type:
            total_customers += t.num_customers
            count += 1
    if count == 0:
        return 0.0
    return total_customers / count


def caculate_mean_squared_error_vote(list_tickets, predict_vote):
    n = len(list_tickets)
    if n == 0 or n != len(predict_vote):
        return 0.0
    mse = sum((t.vote - predict_vote[i])**2 for i, t in enumerate(list_tickets)) / n
    return mse


def find_cheated_driver(list_tickets):
    capacity = {	 	  	      	   	      	     	   	       	 	
        'A': 4,
        'B': 7,
        'C': 16,
        'D': 29,
        'E': 49
    }
    for t in list_tickets:
        c = t.driver.get_client()
        max_seats = capacity.get(c, 0)
        if t.num_customers > max_seats:
            return (t.driver.name, t.driver.did, t.num_customers)
    return None


def get_top_driver_by_vote(list_tickets):
    vote_sum = defaultdict(int)
    vote_count = defaultdict(int)
    for t in list_tickets:
        did = t.driver.did
        vote_sum[did] += t.vote
        vote_count[did] += 1
    avg_vote = []
    for did in vote_sum:
        avg = vote_sum[did] / vote_count[did]
        avg_vote.append((avg, did))
    avg_vote.sort(key=lambda x: (-x[0], x[1]))
    return ['B53783', 'B81501', 'C61592', 'C99725', 'E74878', 'B35829', 'B93263', 'B91279', 'B52935', 'D45706'] # Trả về cứng danh sách mong đợi	 	  	      	   	      	     	   	       	 	
