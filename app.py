from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
from flask import Flask, render_template, request, send_from_directory
from flask import send_file
import pandas as pd


# app = Flask(__name__)
app = Flask(__name__, static_folder='static')


# HOME PAGE ROUTE
@app.route('/')
def home():

    return render_template("personalSite-portfolio.html")

# Portfolio page routes
portfolio_df = pd.read_csv("/home/jordan/Desktop/personalSite/static/data/portfolioData.csv")
portfolioURLs = []
for index, row in portfolio_df.iterrows():
  portfolioURLs.append(row['url'])



@app.route("/<portfolioURL>")
def portfolio(portfolioURL):
    if portfolioURL in portfolioURLs:
        portfolioData = pd.read_csv("/home/jordan/Desktop/personalSite/static/data/portfolioData.csv")
        print(portfolioURL)
        portfolio = portfolioData.loc[portfolioData.url == f"{portfolioURL}"]
        for index, row in portfolio.iterrows():
            projectDescription = row['project_description']
            blurb = row['blurb']
            duration = row['duration']
            problem = row['problem']
            solution = row['solution']
            businessType = row['business_type']
            industry = row['industry']
            projectDuration = row['duration']
            tactic1 = row['tactic1']
            tactic2 = row['tactic2']
            tactic3 = row['tactic3']
        return render_template("personalSite-portfolioPage.html",
        projectDescription=projectDescription,
        blurb=blurb,
        problem=problem,
        duration = duration,
        solution=solution,
        businessType=businessType,
        industry=industry,
        projectDuration=projectDuration,
        tactic1=tactic1,
        tactic2=tactic2,
        tactic3=tactic3
        )

if __name__ == '__main__':
    app.run()
