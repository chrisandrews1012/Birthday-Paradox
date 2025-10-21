import networkx as nx
from datetime import datetime, timedelta
from collections import Counter, defaultdict
from itertools import combinations
import random
import calendar
import math
from decimal import Decimal, getcontext


def random_birthday() -> str:
    """
    Generates a random birthday in the format 'MM_DD' for a non-leap year (2025).

    :return: A random birthday in the format 'MM_DD'.
    :rtype: str
    """
    month = random.randint(1, 12)
    days_in_month = calendar.monthrange(2025, month)[1]
    day = random.randint(1, days_in_month)
    
    return f"{month:02d}_{day:02d}"


def generate_population(num: int) -> list[str]:
    """
    Generates a list of random birthdays in 'MM_DD' string format.

    :param num: The number of individuals in the simulated population.
    :type num: int
    :return: A list of 'num' randomly generated birthday strings,
             each formatted as 'MM_DD' (e.g., '07_21').
    :rtype: list[str]
    """
    population_list = []
    for _ in range(num):
        population_list.append(random_birthday())
        
    return population_list    


def create_graph(population: list[str]) -> nx.Graph:
    """
    Constructs an undirected graph where each node represents a person with a birthday,
    and edges connect people who share the same birthday.

    :param population: A list of birthday strings in 'MM_DD' format.
    :type population: list[str]
    :return: A NetworkX graph where each node is labeled with a unique ID and birthday,
             and edges exist between nodes with matching birthdays.
    :rtype: nx.Graph
    """
    G = nx.Graph()
    bday_groups = defaultdict(list)
    
    for person, bday in enumerate(population):
        G.add_node(person, bday=bday) # Add nodes with attributes
        bday_groups[bday].append(person) # Add person to the defaultdict
        
    # Add edges between nodes sharing the same bday
    for group in bday_groups.values():
        G.add_edges_from(combinations(group, 2))  
        
    return G  


def birthday_paradox_prob(num: int) -> Decimal:
    """
    Calculates the theoretical probability (as a percentage) that at least
      two individuals in a population share the same birthday.

      :param num: The number of individuals in the population.
      :type num: int
      :return: The probability as a percentage that at least two people
               share a birthday. Returns 100 if population exceeds 365 (pigeonhole principle).
      :rtype: Decimal
    """
    getcontext().prec = 15
    
    if num > 365:
          return Decimal('100')  # Pigeonhole Principle
    if num < 2:
          return Decimal('0')  # Need at least 2 people to share
    
    prob_unique = Decimal('1')
    days = Decimal('365')

    for i in range(num):
        prob_unique *= (days - Decimal(i)) / days

    result = Decimal('100') * (Decimal('1') - prob_unique)
    
    if result > Decimal('99.999999999999999'):
        return Decimal('99.999999999999999') 
    else:
        return result

def calculate_prob(population: list[str]) -> tuple[int, int, float]:
    """
    Analyzes a population of birthday strings and computes statistics.

    :param population: A list of birthday strings formatted as 'MM_DD'.
    :type population: list[str]
    :return: A tuple containing:
             - total_bdays (int): Total number of individuals in the population.
             - shared_bdays (int): Number of individuals who share a birthday with at least one other person.
             - percent_bdays (float): Proportion of individuals with a shared birthday, rounded to 5 decimal places.
    :rtype: tuple[int, int, float]
    """
    birthday_counts = Counter(population)
    
    total_bdays = len(population)  
    shared_bdays = sum(count for count in birthday_counts.values() if count > 1)
    percent_bdays = round(shared_bdays / total_bdays, 5)
        
    return total_bdays, shared_bdays, percent_bdays


def birthday_paradox_plot(num):
    """
    Calculates the theoretical probability that at least two people in a group
    of 'num' individuals share the same birthday for plotting purposes.

    :param num: The number of people in the group.
    :type num: int
    :return: The probability (between 0 and 1) that at least two people share a birthday.
             Returns 1.0 if num > 365 due to the pigeonhole principle.
    :rtype: float
    """
    if num > 365:
        return 1
    prob_unique = 1.0
    for i in range(num):
        prob_unique *= (365 - i) / 365
    
    return 1 - prob_unique 
    
    