# PORT RELATED QUERIES
get_port_query = "SELECT code from ports where code='{code}'"
check_port_exists = "SELECT EXISTS(SELECT 1 FROM ports WHERE code='{code}')"
get_port_children_query = "SELECT code from ports where parent_slug in {parents}"

# REGION RELATED QUERIES
get_region_query = "SELECT slug from regions where slug='{slug}'"
check_region_exists = "SELECT EXISTS(SELECT 1 FROM regions WHERE slug='{slug}')"
get_region_children_query = "SELECT slug from regions where parent_slug in {parents}"

# PRICES RELATED QUERIES
get_rates_query = """
    SELECT d.dt, p.avg
        FROM (
            SELECT dt::date FROM generate_series('{date_from}', '{date_to}', '1 day'::interval) dt
        ) d
        LEFT JOIN (
            SELECT prices.day, avg(prices.price) AS avg
            FROM prices where prices.orig_code in {origins} and prices.dest_code in {destinations}
            GROUP by prices.day
            HAVING count(*) >= 3
        ) p on d.dt = p.day
        GROUP by d.dt, p.avg
        ORDER by d.dt;
"""
