import com.mongodb.MongoClient;

import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;

import com.mongodb.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class SimpleStream  implements Runnable{
    static String content;
    static int count=0;
    public static void main(String[] args) {
        String str[]=new String[10];
        for (String strr: args)
        {
            str[0]=strr;
        }
        ConfigurationBuilder cb = new ConfigurationBuilder();
        cb.setDebugEnabled(true);
        cb.setOAuthConsumerKey("9JxIZemKBnnhuMTVX6zHIkV4A");
        cb.setOAuthConsumerSecret("teEnLc5S5ciYgW5bsOkPTY6eL3jUqWekANoS2jboMRoSvVila7");
        cb.setOAuthAccessToken("2912395186-vfIi6kTLvPROZCNFpSxSMshqh5TeR0SX2zZZ8vD");
        cb.setOAuthAccessTokenSecret("047e5jz0o4v6369vDl0qRKaULtajYxTHxwtpnxOWGczng");
        TwitterStream twitterStream = new TwitterStreamFactory(cb.build()).getInstance();
        StatusListener listener = new StatusListener() {
            @Override
            public void onException(Exception arg0) {
                // TODO Auto-generated method stub

            }

            @Override
            public void onDeletionNotice(StatusDeletionNotice arg0) {
                // TODO Auto-generated method stub

            }

            @Override
            public void onScrubGeo(long arg0, long arg1) {
                // TODO Auto-generated method stub

            }
            @Override
            public void onStatus(Status status) {
                User user = status.getUser();
                String username = status.getUser().getScreenName();
                //System.out.println(username);
                String profileLocation = user.getLocation();
                //System.out.println(profileLocation);
                long tweetId = status.getId();
                //System.out.println(tweetId);
                content = status.getText();
                System.out.println(content);
                try{
                    Process p = Runtime.getRuntime().exec("python /home/nill/backend/app/key_predict.py "+ content);
                    InputStreamReader x = new InputStreamReader(p.getInputStream());
                    BufferedReader br = new BufferedReader(x);
                    String line;                   
                    while((line = br.readLine())!= null){
                        System.out.println(line);
                    }
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
                count++;
                if(count>=5)
                    System.exit(0);
            }
            @Override
            public void onTrackLimitationNotice(int arg0) {
                // TODO Auto-generated method stub

            }

            @Override
            public void onStallWarning(StallWarning arg0) {
                // TODO Auto-generated method stub

            }
        };
        FilterQuery fq = new FilterQuery();
        String keyword[] ={str[0]};
        fq.track(keyword);
        fq.language(new String[]{"en"});
        //double [][]location={{-122.75,36.8},{-121.75,37.8}};
        //fq.locations(location);
        twitterStream.addListener(listener);
        twitterStream.filter(fq); 
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
    }
}
