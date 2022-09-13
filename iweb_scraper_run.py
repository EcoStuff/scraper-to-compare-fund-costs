#### ScrapeWebsite_iWeb_ShareDealing iweb_scraper_run.py ####

# This file calls the iweb_scraper methods

from iweb_scraper.iweb_scraper_fundcentre import IWeb_FundCentre

from iweb_scraper.iweb_scraper_datafunctions import IWeb_DataFunctions


import datetime
import time

try:
    with IWeb_FundCentre(teardown=False) as bot:
        #teardown to true if you want webdrive to quit chrome browser after program
        
        # Open first page
        bot.open_landing_page()

        # Show full results
        bot.click_show_results()

        # Click 100 results per page
        #bot.click_100_results_per_page()

        # Get results table
        #print(bot.get_results_table())


        # create collection object with list of list of resutls
        collection = bot.get_results_into_collection()

        # create dataframe from collection 
        df = bot.create_df_from_collection(collection)

        # save dataframe as csv
        bot.save_df_to_csv_file(df)

        # iterate through all iWeb pages
        while int(bot.get_number_of_pages()[0]) < int(bot.get_number_of_pages()[1]):
        #while int(bot.get_number_of_pages()[0]) <= 2: 
            print(f'Page: {bot.get_number_of_pages()[0]} / {bot.get_number_of_pages()[1]}')
            bot.load_next_page_of_results()
            time.sleep(2.5) # pause program for 2.5 seconds

            # Click 100 results per page
            #bot.click_100_results_per_page()

            # read datafrom from csv
            df_1 = bot.read_csv_file_to_df()
            print(df_1)

            # append df1 to df2
            collection = bot.get_results_into_collection()
            df_2 = bot.create_df_from_collection(collection)
            df = bot.concat_df2_to_df1(df_1, df_2)

            bot.save_df_to_csv_file(df)





except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add your selenium Drivers to PATH \n'
            'Windows: \n'
            '   set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '   PATH=$PATH:/path/toyour/folder/ \n'
            )
    else:
        raise
