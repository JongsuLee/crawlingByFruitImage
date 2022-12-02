import streamlit.components.v1 as components

def showCrawled(kurly_dict, gmarket_dict):
    style = '''
    <style>
        * {
            margin: 0;
            padding: 0;
        }
        .outframe {
            width: 700px;
            height: 600px;
            overflow: scroll;
            display: flex;
            padding: 1%;
        }
        
        .itemframe {
            width: 49%;
            padding: 0 1%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .items {
            width: 100%;
            height: inherit;
        }

        .item {
            width: 98%;
            height: inherit;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 5px 0;
            background-color: rgba(220,220,220,0.2);
            text-align: center;
        }

        img {
            width: 300px;
            height: 300px;
            object-fit: cover;
        }

        .title {
            width: 95%;
            height: 1.5rem;
            overflow: hidden;
            word-wrap: break-word;
        }
        
        .prices {
            width: 95%;
            display: flex;
            align-items: center;
            justify-content: space-evenly;
        }

        .price {
            width: 60%;
            font-size: X-large;
            font-weight: bold;
        }
        
        .unitPrice {
            width: 40%;
            font-size: smaller;
            word-wrap: break-word;
        }
    </style>
    '''
    components.html(f'''
        {style}
        <div class="outframe">
            <div class="itemframe">
                <div class="marketname">{"Kurly"}</div>
                <div class="items">
                    <div class="item">
                        <a href="{kurly_dict[1]["url"]}" target="_blank">
                            <img src="{kurly_dict[1]["img"]}" alt="">
                        </a>
                        <div class="title">{kurly_dict[1]["title"]}</div>
                        <div class="prices">
                            <div class="price">{kurly_dict[1]["price"]}</div>
                            <div class="unitprice">{kurly_dict[1]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{kurly_dict[2]["url"]}" target="_blank">
                            <img src="{kurly_dict[2]["img"]}" alt="">
                        </a>
                        <div class="title">{kurly_dict[2]["title"]}</div>
                        <div class="prices">
                            <div class="price">{kurly_dict[2]["price"]}</div>
                            <div class="unitprice">{kurly_dict[2]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{kurly_dict[3]["url"]}" target="_blank">
                            <img src="{kurly_dict[3]["img"]}" alt="">
                        </a>
                        <div class="title">{kurly_dict[3]["title"]}</div>
                        <div class="prices">
                            <div class="price">{kurly_dict[3]["price"]}</div>
                            <div class="unitprice">{kurly_dict[3]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{kurly_dict[4]["url"]}" target="_blank">
                            <img src="{kurly_dict[4]["img"]}" alt="">
                        </a>
                        <div class="title">{kurly_dict[4]["title"]}</div>
                        <div class="prices">
                            <div class="price">{kurly_dict[4]["price"]}</div>
                            <div class="unitprice">{kurly_dict[4]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{kurly_dict[5]["url"]}" target="_blank">
                            <img src="{kurly_dict[5]["img"]}" alt="">
                        </a>
                        <div class="title">{kurly_dict[5]["title"]}</div>
                        <div class="prices">
                            <div class="price">{kurly_dict[5]["price"]}</div>
                            <div class="unitprice">{kurly_dict[5]["unitPrice"]}</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="itemframe">
                <div class="marketname">{"G-market"}</div>
                <div class="items">
                    <div class="item">
                        <a href="{gmarket_dict[1]["url"]}" target="_blank">
                            <img src="{gmarket_dict[1]["img"]}" alt="">
                        </a>
                        <div class="title">{gmarket_dict[1]["title"]}</div>
                        <div class="prices">
                            <div class="price">{gmarket_dict[1]["price"]}</div>
                            <div class="unitprice">{gmarket_dict[1]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{gmarket_dict[2]["url"]}" target="_blank">
                            <img src="{gmarket_dict[2]["img"]}" alt="">
                        </a>
                        <div class="title">{gmarket_dict[2]["title"]}</div>
                        <div class="prices">
                            <div class="price">{gmarket_dict[2]["price"]}</div>
                            <div class="unitprice">{gmarket_dict[2]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{gmarket_dict[3]["url"]}" target="_blank">
                            <img src="{gmarket_dict[3]["img"]}" alt="">
                        </a>
                        <div class="title">{gmarket_dict[3]["title"]}</div>
                        <div class="prices">
                            <div class="price">{gmarket_dict[3]["price"]}</div>
                            <div class="unitprice">{gmarket_dict[3]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{gmarket_dict[4]["url"]}" target="_blank">
                            <img src="{gmarket_dict[4]["img"]}" alt="">
                        </a>
                        <div class="title">{gmarket_dict[4]["title"]}</div>
                        <div class="prices">
                            <div class="price">{gmarket_dict[4]["price"]}</div>
                            <div class="unitprice">{gmarket_dict[4]["unitPrice"]}</div>
                        </div>
                    </div>
                    <div class="item">
                        <a href="{gmarket_dict[5]["url"]}" target="_blank">
                            <img src="{gmarket_dict[5]["img"]}" alt="">
                        </a>
                        <div class="title">{gmarket_dict[5]["title"]}</div>
                        <div class="prices">
                            <div class="price">{gmarket_dict[5]["price"]}</div>
                            <div class="unitprice">{gmarket_dict[5]["unitPrice"]}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    ''', width=700, height=600, scrolling=True)