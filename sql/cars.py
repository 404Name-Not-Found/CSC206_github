class vehicleSQL():

    # Allows display of model and manufacturer
    def all_vehicles(self):
        sql = '''SELECT
                    v.model_name,
                    m.manufacturer_name
                FROM
                    vehicles v
                INNER JOIN
                    manufacturers m 
                ON 
                    v.manufacturerID = m.manufacturerID
                ORDER BY 
                    m.manufacturer_name, v.model_name;'''

        return sql

    # Selects the distinct manufacturer names
    def vehicle_names(self):
        sql = '''Select DISTINCT 
                    m.manufacturer_name
                FROM
                    vehicles
                inner join 
                    csc206cars.manufacturers m 
                on 
                    vehicles.manufacturerID = m.manufacturerID;'''

        return sql

    # Selects the distinct vehicle types
    def vehicle_type(self):
        sql = '''Select DISTINCT 
                    m.vehicle_type_name
                from 
                    vehicles
                inner join 
                    csc206cars.vehicletypes m 
                on 
                    vehicles.vehicle_typeID= m.vehicle_typeID;'''

        return sql

    # Selects model names
    def vehicle_model(self):
        sql = '''Select      
                    model_name
                from 
                    vehicles'''

        return sql

    # Selects fuel type
    def vehicle_fuel_type(self):
        sql = '''Select DISTINCT 
                    fuel_type
                from 
                    vehicles'''

        return sql

    # Select distinct colors
    def colors(self):
        sql = '''SELECT DISTINCT
                    c.color_name
                FROM
                    vehicles
                INNER JOIN 
                    csc206cars.vehiclecolors v
                ON 
                    vehicles.vehicleID = v.vehicleID
                INNER JOIN
                    csc206cars.colors c
                ON
                    v.colorID = c.colorID;
                    '''

        return sql

    # Based on example from template for dynamic routing
    # All the _by_ are used for the displaying of vehicles after you apply a filter
    def vehicles_by_manufacturer(self, manufacturer_name):
        # For how to make a CTE
        # https://hightouch.com/sql-dictionary/sql-common-table-expression-cte
        # The first CTE concatenates the colors and then displays them in alphabetical order
        # The second CTE calculates the total cost of parts for a vehicle
        sql = f'''
            WITH VehicleColorList AS (
                SELECT
                    vc.vehicleID,
                    GROUP_CONCAT(c.color_name ORDER BY c.color_name ASC SEPARATOR ', ') AS concatenated_colors
                FROM
                    csc206cars.vehiclecolors vc
                INNER JOIN
                    csc206cars.colors c 
                ON 
                    vc.colorID = c.colorID
                GROUP BY
                    vc.vehicleID
            ),
            VehiclePartsCost AS (
                SELECT
                    po.vehicleID,
                    SUM(p.cost) AS total_cost
                FROM
                    csc206cars.partorders po
                INNER JOIN
                    csc206cars.parts p 
                ON 
                    po.part_orderID = p.part_orderID
                GROUP BY
                    po.vehicleID
            )
            SELECT
                v.*,
                vcl.concatenated_colors,
                vtn.vehicle_type_name,
                m.manufacturer_name,
                pt.purchase_price,
                vpc.total_cost
            FROM
                csc206cars.vehicles v
            LEFT JOIN
                csc206cars.manufacturers m 
            ON 
                v.manufacturerID = m.manufacturerID
            LEFT JOIN
                csc206cars.vehicletypes vtn 
            ON 
                v.vehicle_typeID = vtn.vehicle_typeID
            LEFT JOIN
                csc206cars.purchasetransactions pt 
            ON 
                v.vehicleID = pt.vehicleID
            LEFT JOIN
                VehiclePartsCost vpc 
            ON 
                v.vehicleID = vpc.vehicleID 
            LEFT JOIN
                VehicleColorList vcl 
            ON 
                v.vehicleID = vcl.vehicleID 
            WHERE
                m.manufacturer_name = '{manufacturer_name}'
            ORDER BY
                v.model_year DESC,
                m.manufacturer_name ASC;
            '''
        return sql

    def sellable_vehicles(self):
        sql = '''
            SELECT
                v.*,
                vcl.concatenated_colors,
                vtn.vehicle_type_name,
                m.manufacturer_name,
                COALESCE(pt.purchase_price, 0.00) AS purchase_price, 
                COALESCE(vpc.total_cost, 0.00) AS total_cost        
            FROM
                csc206cars.vehicles v
            LEFT JOIN
                csc206cars.manufacturers m
            ON
                v.manufacturerID = m.manufacturerID
            LEFT JOIN
                csc206cars.vehicletypes vtn
            ON
                v.vehicle_typeID = vtn.vehicle_typeID
            LEFT JOIN
                csc206cars.purchasetransactions pt
            ON
                v.vehicleID = pt.vehicleID
            LEFT JOIN
                (
                    SELECT
                        po.vehicleID,
                        SUM(p.cost) AS total_cost
                    FROM
                        csc206cars.partorders po
                    INNER JOIN
                        csc206cars.parts p
                    ON
                        po.part_orderID = p.part_orderID
                    GROUP BY
                        po.vehicleID
                ) AS vpc
            ON
                v.vehicleID = vpc.vehicleID
            LEFT JOIN
                (
                    SELECT
                        vc.vehicleID,
                        GROUP_CONCAT(c.color_name ORDER BY c.color_name ASC SEPARATOR ', ') AS concatenated_colors
                    FROM
                        csc206cars.vehiclecolors vc
                    INNER JOIN
                        csc206cars.colors c
                    ON
                        vc.colorID = c.colorID
                    GROUP BY
                        vc.vehicleID
                ) AS vcl
            ON
                v.vehicleID = vcl.vehicleID
            WHERE
                v.vehicleID NOT IN (SELECT vehicleID FROM csc206cars.salestransactions)
                AND
                v.vehicleID NOT IN (
                    SELECT DISTINCT
                        po.vehicleID
                    FROM
                        csc206cars.partorders po
                    INNER JOIN
                        csc206cars.parts p on po.part_orderID = p.part_orderID
                    WHERE
                        p.status != 'Installed'
                )
            ORDER BY
                v.model_year DESC,
                m.manufacturer_name ASC
            '''
        return sql


    def vehicle_by_type(self, vehicle_type_name):
        sql = f'''
            WITH VehiclePartsCost AS (
                SELECT
                    po.vehicleID,
                    SUM(p.cost) AS total_cost
                FROM
                    csc206cars.partorders po
                INNER JOIN
                    csc206cars.parts p 
                ON 
                    po.part_orderID = p.part_orderID
                GROUP BY
                    po.vehicleID
            )
            SELECT 
                    v.*, 
                    v.description,
                    m.manufacturer_name,
                    vtn.vehicle_type_name,
                    pt.purchase_price,
                    vpc.total_cost
                FROM
                    vehicles v
                LEFT JOIN 
                    csc206cars.vehicletypes vtn 
                ON
                    v.vehicle_typeID = vtn.vehicle_typeID
                LEFT JOIN
                    csc206cars.manufacturers m
                ON 
                    v.manufacturerID = m.manufacturerID
                LEFT JOIN
                    csc206cars.purchasetransactions pt
                ON
                    v.vehicleID = pt.vehicleID
                LEFT JOIN
                    VehiclePartsCost vpc 
                ON 
                    v.vehicleID = vpc.vehicleID 
                WHERE
                    vtn.vehicle_type_name = '{vehicle_type_name}'
                ORDER BY
                    v.model_year DESC,
                    m.manufacturer_name ASC;
                '''
        return sql

    def vehicle_by_model(self, model_by_name):
        sql = f'''
            WITH VehiclePartsCost AS (
                SELECT
                    po.vehicleID,
                    SUM(p.cost) AS total_cost
                FROM
                    csc206cars.partorders po
                INNER JOIN
                    csc206cars.parts p 
                ON 
                    po.part_orderID = p.part_orderID
                GROUP BY
                    po.vehicleID
            )
            SELECT
                v.vin,
                v.description,
                v.model_year,
                m.manufacturer_name,
                vtn.vehicle_type_name,
                v.model_name,
                pt.purchase_price,
                vpc.total_cost
            FROM
                vehicles v
            LEFT JOIN 
                csc206cars.manufacturers m
            ON  
                v.manufacturerID = m.manufacturerID
            LEFT JOIN
                csc206cars.vehicletypes vtn
            ON  
                v.vehicle_typeID = vtn.vehicle_typeID
            LEFT JOIN
                csc206cars.purchasetransactions pt
            ON
                v.vehicleID = pt.vehicleID
            LEFT JOIN
                VehiclePartsCost vpc 
            ON 
                v.vehicleID = vpc.vehicleID 
            WHERE 
                model_name = '{model_by_name}'
            ORDER BY
                v.model_year DESC,
                m.manufacturer_name ASC;   
                '''
        return sql

    def vehicle_by_fuel(self, fuel_by_type):
        sql = f'''
            WITH VehiclePartsCost AS (
                SELECT
                    po.vehicleID,
                    SUM(p.cost) AS total_cost
                FROM
                    csc206cars.partorders po
                INNER JOIN
                    csc206cars.parts p 
                ON 
                    po.part_orderID = p.part_orderID
                GROUP BY
                    po.vehicleID
            )
            SELECT 
                    v.fuel_type,
                    v.vin,
                    v.model_year,
                    v.description,
                    m.manufacturer_name,
                    vtn.vehicle_type_name,
                    v.model_name,
                    pt.purchase_price,
                    vpc.total_cost
                FROM
                    vehicles v
                LEFT JOIN
                    csc206cars.manufacturers m 
                ON
                    v.manufacturerID = m.manufacturerID
                LEFT JOIN
                    csc206cars.vehicletypes vtn
                ON 
                    v.vehicle_typeID = vtn.vehicle_typeID   
                LEFT JOIN
                    csc206cars.purchasetransactions pt
                ON
                    v.vehicleID = pt.vehicleID
                LEFT JOIN
                    VehiclePartsCost vpc 
                ON 
                    v.vehicleID = vpc.vehicleID 
                WHERE 
                    fuel_type = '{fuel_by_type}'
                ORDER BY
                    v.model_year DESC,
                    m.manufacturer_name ASC;   
                    '''

        return sql

    def vehicle_by_color(self, color_name):
        sql = f'''
            WITH VehiclePartsCost AS (
                SELECT
                    po.vehicleID,
                    SUM(p.cost) AS total_cost
                FROM
                    csc206cars.partorders po
                INNER JOIN
                    csc206cars.parts p 
                ON 
                    po.part_orderID = p.part_orderID
                GROUP BY
                    po.vehicleID
            )
            SELECT
                     v.*,
                     c.color_name,
                    pt.purchase_price,
                    vpc.total_cost,
                    m.manufacturer_name
                    
                FROM
                    csc206cars.vehicles v
                LEFT JOIN 
                    csc206cars.manufacturers m
                ON
                    v.manufacturerID = m.manufacturerID
                LEFT JOIN 
                    csc206cars.vehiclecolors vc
                ON 
                    v.vehicleID = vc.vehicleID
                LEFT JOIN
                    csc206cars.colors c
                ON
                    vc.colorID = c.colorID
                LEFT JOIN
                    csc206cars.purchasetransactions pt
                ON
                    v.vehicleID = pt.vehicleID
                LEFT JOIN
                    VehiclePartsCost vpc 
                ON 
                    v.vehicleID = vpc.vehicleID 
                WHERE 
                    c.color_name = '{color_name}'
                ORDER BY
                    v.model_year DESC,
                    m.manufacturer_name ASC;   
                 '''

        return sql

    # 3 Queries below done with help of ma boi
    def sale(self):
        sql = '''
            SELECT 
                u.userID, 
                CONCAT(u.first_name, ' ', u.last_name) AS salesperson, 
                COUNT(s.vehicleID) AS vehicles_sold, 
                COALESCE(SUM(pt.purchase_price),0) AS total_sold_price, 
            CASE WHEN 
                COUNT(s.vehicleID) > 0 
            THEN 
                COALESCE(SUM(pt.purchase_price),0)/COUNT(s.vehicleID) ELSE NULL END AS avg_sale_price 
            FROM 
                salestransactions s 
            JOIN 
                users u 
            ON
                s.userID = u.userID 
            LEFT JOIN 
                purchasetransactions pt 
            ON 
                s.vehicleID = pt.vehicleID 
            GROUP BY 
                u.userID, u.first_name, u.last_name 
            ORDER BY 
                vehicles_sold DESC, 
                total_sold_price DESC;
            '''

        return sql

    def seller(self):
        sql = '''     
            SELECT 
                c.customerID, 
                CONCAT(c.first_name, ' ', c.last_name) AS seller_name, 
                COUNT(pt.vehicleID) AS vehicles_sold_to_dealer, 
                COALESCE(SUM(pt.purchase_price),0) AS total_paid 
            FROM 
                purchasetransactions pt 
            JOIN 
                customers c 
            ON 
                pt.customerID = c.customerID 
            GROUP BY 
                c.customerID, c.first_name, c.last_name 
            ORDER BY 
                vehicles_sold_to_dealer DESC, 
                total_paid ASC;
            '''
        return sql

    def statistics(self):
        sql = '''
            SELECT 
                v.vendorID, 
                v.vendor_name, 
                COALESCE(SUM(p.quantity),0) AS parts_purchased, 
                COALESCE(SUM(p.cost * p.quantity),0.00) AS total_spent, 
        CASE WHEN 
            SUM(p.quantity) > 0 
        THEN 
            SUM(p.cost * p.quantity)/SUM(p.quantity) ELSE NULL END AS avg_cost_per_part 
        FROM 
            partorders po 
        JOIN 
            vendors v 
        ON 
            po.vendorID = v.vendorID 
        JOIN
            parts p 
        ON 
            p.part_orderID = po.part_orderID 
        GROUP BY 
            v.vendorID, 
            v.vendor_name 
        ORDER BY 
            parts_purchased DESC;
        '''
        return sql