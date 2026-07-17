# tests.py
import unittest
import os
from bs4 import BeautifulSoup

os.environ['TESTING'] = 'true'

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        # print(f"html : {html}")
        assert "<title>Helia Dinh</title>" in html
        
        soup = BeautifulSoup(html, "html.parser")
        nav = soup.find("ul", class_ = "site-navigation-links")
        assert nav is not None
        
        # Nav tests
        links = nav.find_all("a")
        print(f"links : {links[0]}")
        hrefs = [a["href"] for a in links]
        texts = [a.get_text(strip=True) for a in links]
        
        assert hrefs == ["/","/hobbies","/map","/timeline",]
        assert texts == ["Home","Projects & Hobbies","Map","Timeline"]
        
        assert links[0].get("aria-current") == "page"
        assert links[1].get("aria-current") == None
        
        # profile tests
        profile_div = soup.find("div", class_ = "nav-logo")
        print(f"profile_div : {profile_div}")
        image = profile_div.find("img")
        print(f"img : {image}")
        assert image["src"] is not ""
        assert image["alt"] is not ""
        
        # image tests
        images = soup.find_all("img")
        sources = [img["src"] for img in images]
        alt_texts = [img["alt"] for img in images]
        for src in sources:
            assert src is not ""
        for text in alt_texts:
            assert text is not ""
            
        # href tests
        hrefs = soup.find_all("a")
        paths = [a["href"] for a in hrefs]
        for path in hrefs:
            assert path is not ""
        
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        print(f"json-timeline : {json}")
        assert "timeline_posts" in json
        # assert len(json["timeline_posts"]) == 0
        
        post_response = self.client.post("/api/timeline_post",data={
            "name":"susan rosh",
            "email":"susan@example.com",
            "content":"Hello world, I\'m Susan!"
        })
        print(f"post : {post_response}")
        assert post_response.status_code == 200
        json = post_response.get_json()
        print(f"post response : {json}")
        assert json['name'] == 'susan rosh'
        assert json['email'] == 'susan@example.com'
        
        
        # Timeline page tests
        
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        # print(f"html : {html}")
        
        assert "<title>Timeline</title>" in html
        
        soup = BeautifulSoup(html, "html.parser")
        
        # image tests
        images = soup.find_all("img")
        sources = [img["src"] for img in images]
        alt_texts = [img["alt"] for img in images]
        for src in sources:
            assert src is not ""
        for text in alt_texts:
            assert text is not ""
            
        # href tests
        hrefs = soup.find_all("a")
        paths = [a["href"] for a in hrefs]
        for path in paths:
            assert path is not ""
            
        # form tests
        labels = soup.find_all("label")
        label_for = [label["for"] for label in labels]
        for item in label_for:
            assert item != ""
        
        inputs = soup.find_all("input")
        content = [[input["id"],input["name"],input["type"]] for input in inputs]
        for data in content:
            print(f"input data : {data}")
            assert data[0] != ""
            assert data[1] != ""
            assert data[2] != ""
            
        # button tests
        submit_button = soup.find("button", class_="timeline-submit")
        assert submit_button["type"] == "submit"
        
    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post",data={
            "email":"john@example.com",
            "content":"Hello world, I am John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        response = self.client.post("/api/timeline_post",data={
            "name":"susan rosh",
            "email":"susan@example.com",
            "content":""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html
        
        response = self.client.post("/api/timeline_post",data={
            "name":"susan rosh",
            "email":"not-an-email",
            "content":"Hello world, I\'m Susan!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
        
        
        