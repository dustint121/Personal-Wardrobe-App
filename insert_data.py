from backend import queries
import pyodbc

if __name__ == "__main__":
    conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-KHUP1V2;DATABASE=Wardrobe;Trusted_Connection=yes")

    queries.add_clothing_piece(conn, short_descriptor="Plaid Linen Jacket", brand="Polo by Ralph Lauren", category="Jacket", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2023/05/17/6464d684b635f8b52908d1aa/m_wp_6464d685b635f8b52908d1b5.webp")
    queries.add_clothing_piece(conn, short_descriptor="Linen Lounge/Sleep Shorts Navy", brand="J. Crew", category="Shorts", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2023/04/19/6440086bfed51fa6c85690ef/m_wp_6440086c97b5d0afe68ac598.webp")
    queries.add_clothing_piece(conn, short_descriptor="Linen Lounge/Sleep Shorts Orange-Striped", brand="J. Crew", category="Shorts", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2023/05/26/64710e3fc1c346b5cc55607a/m_wp_64710e41614973bdfba1788c.webp")
    queries.add_clothing_piece(conn, short_descriptor="Plaid Sweater", brand="Zenetto", category="Sweater", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2023/02/26/63fbe9a3acb9f51ffd36fccc/m_wp_63fbe9a3acb9f51ffd36fccd.webp")
    queries.add_clothing_piece(conn, short_descriptor="Linen Striped Tanktop", brand="Madewell", category="Tanktop", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2022/03/02/621f9374cb23aa40473220eb/m_wp_621f93786f6c91509096937d.webp")
    queries.add_clothing_piece(conn, short_descriptor="Linen Blend Houndstooth Pants ", brand="A&F", category="Pants", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2022/11/06/63681fb5acf462364c9f0e07/m_wp_63681fc5308f0763fae7808a.webp")
    queries.add_clothing_piece(conn, short_descriptor="Linen Blend Pants Navy", brand="Jomers", category="Pants", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2020/10/25/5f96680d12d880c2637f4cc3/m_5f96681c4fd23aea0db96be3.jpg")
    queries.add_clothing_piece(conn, short_descriptor="White Linen Vacay Button Down Shirt", brand="Tommy Bahama", category="Buttoned Shirt", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2023/04/17/643e001193a13d088ead4680/m_wp_643e0013c9a22891c4b66f42.webp")
    queries.add_clothing_piece(conn, short_descriptor="2-Tone Blue Polo", brand="Fred Perry", category="Polo Shirt", 
                               url="https://di2ponv0v5otw.cloudfront.net/posts/2023/03/01/63ffc5b22fbf1a9f2d25dafd/m_wp_63ffc5e597b5d0074df5679c.webp")

