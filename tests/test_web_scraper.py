from web_scraper.scraper import url1, url,get_citations_needed_count,get_citations_needed_report
from web_scraper import __version__


def test_version():
    assert __version__ == '0.1.0'



def test_get_citations_needed_count():
    actual0 = get_citations_needed_count(url)
    actual1 = get_citations_needed_count(url1)
    expected0 = 5
    expected1 = 2
    assert  actual0 == expected0
    assert  actual1 == expected1


def test_get_citations_needed_report():
    actual0 = get_citations_needed_report(url)
    actual1 = get_citations_needed_report(url1)
    expected1 = 'The king of Zhou at this time invoked the concept of the Mandate of Heaven to legitimize his rule, a concept that was influential for almost every succeeding dynasty.[citation needed] Like Shangdi, Heaven (tian) ruled over all the other gods, and it decided who would rule China.[34] It was believed that a ruler lost the Mandate of Heaven when natural disasters occurred in great number, and when, more realistically, the sovereign had apparently lost his concern for the people. In response, the royal house would be overthrown, and a new house would rule, having been granted the Mandate of Heaven.'
    expected0 = "During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] Europeans, Africans, and indigenous intermixed, creating a mixed-race casta population in a process known as mestizaje. Mestizos, people of mixed European-indigenous ancestry, constitute the majority of Mexico's population."
    assert  expected0 in actual0
    assert  expected1 in actual1