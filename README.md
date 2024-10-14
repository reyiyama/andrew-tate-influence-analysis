# Analyzing Andrew Tate's Digital Influence

<img width="1104" alt="Screenshot 2024-10-15 at 12 47 50 AM" src="https://github.com/user-attachments/assets/d02bf8c0-86e4-4799-a6c6-a9e78affc102">


### Project Overview
In this project, we analyzed the online influence of Andrew Tate using data from YouTube and Reddit. Our analysis spanned multiple facets including sentiment analysis, topic modeling, and network analysis. We used a variety of data science tools to understand the online discourse surrounding Andrew Tate, who is a controversial figure known for his polarizing opinions on gender roles and masculinity. Given the widespread nature of misinformation and propaganda today, we believe that such an analysis can provide crucial insights into how influential figures shape public opinion online.

### Data Collection
We collected data from two main platforms: Reddit and YouTube. For YouTube, we employed the YouTube API to gather comments, replies, and metadata related to videos discussing Andrew Tate. Similarly, for Reddit, we gathered posts and comments from relevant subreddits. This data provided us with a rich corpus for analysis, spanning both textual content and user engagement metrics.

- **Reddit Data Collection**: We used the Reddit API to gather posts and comments mentioning Andrew Tate across various subreddits. We also pre-processed the collected data by tokenizing, removing stopwords, and stemming tokens using custom Python scripts, centralizing all preprocessing operations into one reusable class.
- **YouTube Data Collection**: Using YouTube API endpoints, we gathered comments and replies on videos that had discussions on Andrew Tate. The data collection involved setting up API request loops to gather as many comments as possible, respecting rate limits by adding delay as required.

### Data Preprocessing
For preprocessing Reddit and YouTube data, we utilized Python classes and a custom pipeline to ensure clean and consistent data. Key steps included:
- **Tokenization**: We utilized NLTK's TweetTokenizer to split text into tokens, removing punctuations and special characters.
- **Stopword Removal and Lemmatization**: We removed common stopwords, including custom terms specific to Reddit and YouTube content, and applied lemmatization using WordNetLemmatizer to reduce words to their base forms.
- **Further Filtering**: We applied additional filters to remove numeric data, URLs, and emojis to keep the analysis focused on meaningful content.

### Sentiment Analysis
We conducted a sentiment analysis to determine how people feel about Andrew Tate. We used a "count word sentiment analysis" method, where we used sets of positive and negative words to score the sentiment of each post or comment. Each Reddit or YouTube comment was pre-processed to extract tokens, and then we counted occurrences of positive and negative terms to compute the overall sentiment.

### Topic Modeling
We employed Latent Dirichlet Allocation (LDA) to identify major topics present in the discussions about Andrew Tate. This involved using both the Gensim library and scikit-learn's LDA model to:
- Preprocess the text corpus using a custom tokenizer and stopwords list.
- Fit an LDA model to identify key themes in discussions, such as gender dynamics, relationships, and societal values.
- Visualize the extracted topics through word clouds to better understand the context of each topic.

<img width="909" alt="Screenshot 2024-10-15 at 12 45 16 AM" src="https://github.com/user-attachments/assets/e973c384-4f2a-4b95-8df8-d3f52f4260d6">

The topic modeling helped us uncover the recurring themes surrounding Tate's content, such as masculinity, relationships, and controversy over social and political views.

### Network Analysis with Gephi
We visualized the network structure of interactions involving Andrew Tate's discussions using Gephi. Specifically, we:
- Constructed a directed graph with nodes representing users and edges representing interactions (e.g., comments or replies).
- Exported data from Python to GraphML format and imported it into Gephi for visualization.
- Ran network metrics such as degree centrality, betweenness centrality, and community detection to understand influential nodes (users) and detect clusters in the online discourse.

<img width="765" alt="Screenshot 2024-10-15 at 12 46 48 AM" src="https://github.com/user-attachments/assets/efdd6957-26b4-4164-9495-b1c10707595d">


These network visualizations provided a visual representation of the level of engagement, allowing us to observe patterns like which videos generated the most interactions or how specific communities reacted to Tate's views.

### Findings
Our analysis revealed several interesting insights:
- **Polarizing Influence**: Sentiment analysis showed a highly polarized audience, with both extreme positive and negative sentiments dominating discussions.
- **Echo Chambers**: Network analysis uncovered community clusters that appear to be echo chambers, where users share similar views and reinforce each other’s beliefs, often amplifying divisive content.
- **Topic Insights**: Topic modeling highlighted themes such as "toxic masculinity," "freedom of speech," and "relationship dynamics," providing insights into why Andrew Tate's views appeal to certain demographics.

### Why This Analysis Matters
In today's world, individuals like Andrew Tate wield significant influence through social media, where misinformation and propaganda can spread unchecked. By analyzing such figures, we can:

- **Understand Online Radicalization**: The analysis of Andrew Tate's influence provides critical insight into the mechanisms of online radicalization, particularly through platforms like YouTube and Reddit. According to Pew Research Center, social media usage is still prevalent, with platforms like YouTube and Reddit experiencing significant growth【25†source】. This is crucial because these platforms have become central in the dissemination of content related to polarizing figures, serving as breeding grounds for radicalization by leveraging algorithms that amplify sensational and divisive content.

<img width="694" alt="Screenshot 2024-10-15 at 12 40 10 AM" src="https://github.com/user-attachments/assets/eb90d46d-667c-4396-8e89-3e0bd82a0576">


- **The Manosphere and Its Impact**: A significant portion of the discussions analyzed falls under the broader category of the "manosphere," which refers to a network of online communities that propagate extreme misogynistic ideologies. The Institute for Strategic Dialogue (ISD) notes that the manosphere is deeply interconnected with other extremist movements, often sharing language and ideology with right-wing groups【26†source】. By understanding the nature of Andrew Tate's content, which aligns with this broader ecosystem of misogynistic discourse, we gain insight into the dynamics of the manosphere that draw individuals in, offering simplistic solutions to complex issues like personal failure and masculinity in crisis. This provides a gateway for users to potentially become more entrenched in far-right or extremist ideologies.

- **Inform Countermeasures and Interventions**: By identifying the recurring themes and network structures in the discourse, policymakers, social platforms, and activists can better understand where misinformation and divisive rhetoric are most prevalent and how to design effective interventions. The influence of thought leaders within the manosphere has been compared to a form of "ontological security racketeering," where figures like Andrew Tate create cycles of insecurity and then present themselves as the solution, drawing in audiences who are looking for a sense of belonging and identity【27†source】. Understanding these dynamics is crucial for developing counter-narratives that address the insecurities and grievances of these audiences.

- **Identify Echo Chambers and Their Effects**: Network analysis plays a vital role in identifying echo chambers—communities where similar views are constantly reinforced, often leading to more extreme viewpoints. As highlighted by Fast Capitalism's analysis, influential figures within the manosphere, such as Andrew Tate, perpetuate cycles of ontological insecurity and re-security, thus maintaining and growing their audience by exploiting their anxieties about masculinity and societal changes【27†source】. Recognizing these echo chambers is critical because they serve as incubators for radicalization, where users are shielded from alternative perspectives and instead fed a steady diet of ideologically homogeneous content.

<img width="952" alt="Screenshot 2024-10-15 at 12 43 43 AM" src="https://github.com/user-attachments/assets/e5090ebd-4c67-4010-967a-6de096f3f9db">


- **Addressing the Societal Impact of Misinformation and Propaganda**: Our analysis underscores the importance of monitoring and analyzing influential online figures like Andrew Tate, particularly in a misinformation-heavy environment. Social media allows for the rapid spread of false narratives and emotional appeals that can escalate into real-world consequences. As seen in various tragic instances documented by the ISD, the manosphere has ties to real-world violence and terrorism, such as the incel movement and attacks inspired by their ideology【26†source】. Analyzing figures like Tate helps us understand how rhetoric can move from being online discourse to inciting or justifying real-world violence.

<img width="681" alt="Screenshot 2024-10-15 at 12 42 47 AM" src="https://github.com/user-attachments/assets/7faa4807-32bf-4766-8a44-5de9bf031dd4">

Through the combination of sentiment analysis, topic modeling, and network analysis, this project provides a comprehensive view of the online influence of controversial figures. It reveals how their influence can contribute to broader societal issues, such as radicalization, misogyny, and the reinforcement of toxic cultural norms. Using visualizations to understand these networks and their spread provides an essential tool for combating the negative impact of such ideologies.


### How to Reproduce This Analysis
If you want to conduct a similar analysis or reproduce our results, follow these steps in detail:

1. **Data Collection**:
   - **YouTube Data Collection**:
     1. Obtain a YouTube API key from Google Cloud Console.
     2. Install the required Python packages: `pip install requests pandas`.
     3. Create a Python script (`youtube_data_collection.py`) and add the following code:
        ```python
        import requests
        import time
        import pandas as pd
        
        SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
        COMMENTS_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
        API_KEY = 'YOUR_API_KEY'
        
        def make_request(url, params):
            while True:
                response = requests.get(url, params=params)
                if response.status_code == 403 and 'quota' in response.text:
                    print("Rate limit hit. Sleeping for 3600 seconds...")
                    time.sleep(3600)
                    continue
                return response
        
        # Collect video data
        search_params = {
            'part': 'snippet',
            'q': 'Andrew Tate',
            'type': 'video',
            'key': API_KEY,
            'maxResults': 50
        }
        
        videos = []
        while True:
            response = make_request(SEARCH_URL, search_params)
            results = response.json()
            videos.extend(results.get('items', []))
            
            page_token = results.get('nextPageToken')
            if not page_token:
                break
            search_params['pageToken'] = page_token
        
        # Collect comments data for each video
        df_data = []
        for video in videos:
            video_id = video['id']['videoId']
            video_name = video['snippet']['title']
            comments = []
            page_token = None
            
            while True:
                params = {
                    'part': 'snippet,replies',
                    'videoId': video_id,
                    'key': API_KEY,
                    'pageToken': page_token
                }
                
                comments_response = make_request(COMMENTS_URL, params)
                comments_data = comments_response.json()
                comments.extend(comments_data.get('items', []))
                
                page_token = comments_data.get('nextPageToken')
                if not page_token:
                    break
                
            # Add comment details to df_data
            for comment in comments:
                topLevelComment = comment['snippet']['topLevelComment']['snippet']
                comment_id = comment['id']
                comment_likes = topLevelComment['likeCount']
                df_data.append({
                    'ID': comment_id,
                    'ParentID': video_id,
                    'Type': 'comment',
                    'Content': topLevelComment['textDisplay'],
                    'Upvotes': comment_likes,
                    'Date': topLevelComment['publishedAt'],
                    'VideoName': video_name
                })
        
        # Save data to CSV
        df = pd.DataFrame(df_data)
        df.to_csv("Tate_youtube.csv", index=False)
        ```
     4. Run the script to gather YouTube data.

   - **Reddit Data Collection**:
     1. Obtain a Reddit API key by creating an app at https://www.reddit.com/prefs/apps.
     2. Install the required Python packages: `pip install praw pandas`.
     3. Create a Python script (`reddit_data_collection.py`) and add the following code:
        ```python
        import praw
        import pandas as pd
        
        reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                             client_secret='YOUR_CLIENT_SECRET',
                             user_agent='YOUR_USER_AGENT')
        
        subreddit = reddit.subreddit('all')
        query = 'Andrew Tate'
        posts = subreddit.search(query, limit=1000)
        
        data = []
        for post in posts:
            comments = post.comments
            for comment in comments:
                if isinstance(comment, praw.models.Comment):
                    data.append({
                        'ID': comment.id,
                        'ParentID': post.id,
                        'Type': 'comment',
                        'Content': comment.body,
                        'Upvotes': comment.score,
                        'Date': comment.created_utc,
                        'Subreddit': post.subreddit.display_name
                    })
        
        # Save data to CSV
        df = pd.DataFrame(data)
        df.to_csv("Tate_reddit.csv", index=False)
        ```
     4. Run the script to gather Reddit data.

2. **Data Preprocessing**:
   1. Install the required Python packages: `pip install nltk`.
   2. Use the following Python code to preprocess both Reddit and YouTube data:
      ```python
      import pandas as pd
      from nltk.tokenize import TweetTokenizer
      from nltk.corpus import stopwords
      from nltk.stem import WordNetLemmatizer
      import string
      
      # Load data
      df = pd.read_csv("Tate_youtube.csv")
      
      # Initialize tokenizer, lemmatizer, and stopwords
      tokenizer = TweetTokenizer()
      lemmatizer = WordNetLemmatizer()
      stop_words = set(stopwords.words('english') + list(string.punctuation))
      
      def preprocess(text):
          tokens = tokenizer.tokenize(text.lower())
          tokens = [lemmatizer.lemmatize(tok) for tok in tokens if tok not in stop_words and tok.isalpha()]
          return ' '.join(tokens)
      
      # Apply preprocessing
      df['Processed_Content'] = df['Content'].apply(preprocess)
      df.to_csv("Tate_youtube_processed.csv", index=False)
      ```

3. **Sentiment Analysis**:
   1. Define positive and negative word lists in a text file (`positive-words.txt`, `negative-words.txt`).
   2. Use the following Python script to perform sentiment analysis:
      ```python
      import pandas as pd
      
      # Load data
      df = pd.read_csv("Tate_youtube_processed.csv")
      
      # Load positive and negative words
      with open("positive-words.txt", "r") as file:
          pos_words = set(file.read().splitlines())
      with open("negative-words.txt", "r") as file:
          neg_words = set(file.read().splitlines())
      
      def compute_sentiment(text):
          tokens = text.split()
          pos_count = sum(1 for tok in tokens if tok in pos_words)
          neg_count = sum(1 for tok in tokens if tok in neg_words)
          return pos_count - neg_count
      
      # Apply sentiment analysis
      df['Sentiment'] = df['Processed_Content'].apply(compute_sentiment)
      df.to_csv("Tate_youtube_sentiment.csv", index=False)
      ```

4. **Topic Modeling**:
   1. Install the required Python packages: `pip install gensim`.
   2. Use the following Python script to perform topic modeling:
      ```python
      import pandas as pd
      from gensim import corpora
      from gensim.models.ldamodel import LdaModel
      from gensim.parsing.preprocessing import STOPWORDS
      
      # Load data
      df = pd.read_csv("Tate_youtube_processed.csv")
      
      # Preprocess data for LDA
      texts = [text.split() for text in df['Processed_Content']]
      dictionary = corpora.Dictionary(texts)
      corpus = [dictionary.doc2bow(text) for text in texts]
      
      # Train LDA model
      lda_model = LdaModel(corpus=corpus, num_topics=5, id2word=dictionary, passes=10)
      lda_model.save("tate_lda_model")
      
      # Print topics
      topics = lda_model.print_topics()
      for topic in topics:
          print(topic)
      ```

5. **Network Analysis**:
   1. Install the required Python packages: `pip install networkx`.
   2. Use the following Python script to build and export the network:
      ```python
      import pandas as pd
      import networkx as nx
      
      # Load data
      df = pd.read_csv("Tate_youtube.csv")
      
      # Create directed graph
      G = nx.DiGraph()
      for index, row in df.iterrows():
          G.add_node(row['ID'], type=row['Type'], content=row['Content'], upvotes=row['Upvotes'], date=row['Date'])
          if row['ParentID']:
              G.add_edge(row['ParentID'], row['ID'], weight=row['Upvotes'])
      
      # Export to GraphML
      nx.write_graphml(G, "Tate_network.graphml")
      ```
   3. **Using Gephi**:
      - **Step 1**: Open Gephi and create a new project.
      - **Step 2**: Import the `Tate_network.graphml` file by selecting "File > Open" and choosing the file.
      - **Step 3**: In the "Import Report" window, select "Directed Graph" and click "OK".
      - **Step 4**: Run the **Layout** algorithms to visualize the network, such as **Force Atlas** or **Yifan Hu**.
      - **Step 5**: Apply **Statistics** to calculate metrics like degree centrality and modularity to identify influential nodes and communities.
      - **Step 6**: Use the **Partition** and **Ranking** modules to highlight nodes based on their attributes, such as upvotes or types.
      - **Step 7**: Export visualizations as PNG or SVG files for reporting.

### Tools & Libraries Used
- **Python** for data scraping, processing, and analysis.
- **NLTK, Gensim, Scikit-learn** for text processing, sentiment analysis, and topic modeling.
- **NetworkX and Gephi** for network construction and visualization.
- **Pandas** for data manipulation and **Matplotlib** for basic visualizations.
- **Gephi** for Network Visualization



### Conclusion

1. **Hypothesis Verification**: The sentiment analysis corroborates our initial hypothesis and findings. The digital discourse around Tate oscillates between support and criticism, underscoring the effectiveness of ontological security theory in shaping and driving these sentiments, which further aligns with the model presented by Bujalka et al. (2022).

2. **Research Synopsis**: The sentiment analysis emphasizes Tate's prowess in manipulating ontological insecurities. Through the identified topics, it becomes evident that Tate manages to evoke a sense of threat to masculinity, offering remedies that potentially lead to tangible benefits for him. This dynamic fosters a spectrum of sentiments, both positive and negative, around his persona.

3. **Recommendations for Future Exploration**: Given the efficacy of the sentiment analysis approach, future research might consider broadening its scope to other platforms where Tate is active. Additionally, integrating more qualitative methods, such as interviews or focused group discussions, would deepen the understanding of the sentiments and their origins.

4. **Learnings and Implications**: The sentiment analysis underscores the potent influence digital personalities wield in shaping online perceptions. Figures like Tate exploit the interplay of insecurities and solutions, crafting vast digital networks. Recognizing and understanding these patterns is vital as the digital realm becomes more deeply ingrained in societal dynamics. The research serves as a clarion call for stakeholders to invest in more robust digital literacy education and tools that can empower users to critically analyze and differentiate between genuine online interactions and those manipulated for personal or commercial gain.

Moreover, the proliferation of digital influences and personalities can have profound impacts on the mental well-being of users, especially younger audiences. The constant exposure to curated lives and narratives can foster unrealistic expectations, potentially leading to feelings of inadequacy, anxiety, and depression. Therefore, it becomes imperative for platforms hosting such content to introduce safeguards, guidelines, and support systems to mitigate potential harm. Furthermore, the nature of online interactions and their influence on real-world behavior underscores the need for ethical considerations. Digital personalities, while potentially offering a vast range of benefits like entertainment, education, and social connections, also carry the risk of propagating misinformation, biases, and harmful stereotypes. Platforms and influencers should take on the responsibility of ensuring the content they produce and share aligns with ethical standards. Collaborative efforts between tech companies, policymakers, educators, and mental health professionals can pave the way for a more balanced and conscious online environment. This might include the creation of toolkits for parents and educators to navigate the digital landscape, guidelines for digital influencers to ensure they operate within ethical boundaries, and platform-based interventions that promote positive online behaviors.

In conclusion, the digital age presents both unprecedented opportunities and challenges. Embracing its benefits requires a proactive approach in addressing its potential pitfalls. The findings of this sentiment analysis reinforce the importance of continuous research, monitoring, and intervention to ensure a healthy and constructive digital experience for all users.

------

Feel free to clone this repository and use our scripts to explore similar topics. Contributions and suggestions are always welcome!
