html_code = '''
    <div style="display: flex; justify-content: center;">
        <div style="width: 50%;text-align:left">
            <strong>Filters:</strong>
            <p></p>
            <p>Gender: Passenger's gender (male, female).</p>
            <p>Age: Passengers' age on the Titanic.</p>
            <p>Survived: Indicates passenger survival status.</p>
        </div>
        <div style="width: 50%;text-align:left">
            <strong>Metrics:</strong>
            <p></p>
            <p>Total: The total number of people or categorized by gender.</p>
            <p>Average Age: The average age of all passengers or categorized by gender.</p>
            <p>Total Survived: The total number of survivors among all passengers or categorized by gender.</p>
        </div>
    </div>
    '''

css_style = """
<style>
     .custom-column {
        margin: 20px;
    }

    .subheader {
        font-size: 24px;
        font-weight: bold;
        margin-top: 50px;
        margin-bottom:50px
    }

.subheader-2 {
        font-size: 21px;
        font-weight: bold;
        margin-top: 50px;
        margin-bottom:50px
    }

// KPI METRICS //
    .div-container{
    display: flex;
    margin: 10px
    background-color: #F9F9F9;

}
.div-icon{
    border-radius: 50%;
    width: 100px;
    height:100px; 
     flex-shrink: 0;
    background-color: #3CA0FF;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 1%;
}

.icon-img{
    max-width: 50%;
    max-height: 50%;
    float: left

}

.header{
    font-size: 15px;

}

.text{
    font-size: 26px;
    font-weight: bold;
    line-height: 2px;

}

.container {
  text-align: center;
  position: relative;
}

.container p {
  position: relative;
  z-index: 2;
}

.container img {
  position: relative;
  top: 20px; /* Adjust this value as needed */
  right: 5px
}


.centered-columns {
    display: flex;
    justify-content: center;
}

</style>
"""
title= {
    "statistics":'<p class="subheader">Statistics</p>',
}