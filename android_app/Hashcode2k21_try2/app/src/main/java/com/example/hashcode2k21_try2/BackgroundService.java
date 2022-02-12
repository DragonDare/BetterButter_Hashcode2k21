package com.example.hashcode2k21_try2;

import static com.example.hashcode2k21_try2.MainActivity.DISCORD_COUNTER;
import static com.example.hashcode2k21_try2.MainActivity.WHATSAPP_COUNTER;

import android.app.Service;
import android.app.usage.UsageStats;
import android.app.usage.UsageStatsManager;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.IBinder;

import androidx.annotation.Nullable;

import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

public class BackgroundService extends Service {

    private SharedPreferences sharedPreferences;
    private SharedPreferences.Editor editor;
    public BackgroundService(){

    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        sharedPreferences = getSharedPreferences("Hashcode2k21_try2", MODE_PRIVATE);
        editor = sharedPreferences.edit();
        TimerTask detectApp = new TimerTask() {
            @Override
            public void run() {
                sharedPreferences = getSharedPreferences("Hashcode2k21_try2", MODE_PRIVATE);
                editor = sharedPreferences.edit();
                UsageStatsManager usageStatsManager = (UsageStatsManager)getApplicationContext().getSystemService(getApplicationContext().USAGE_STATS_SERVICE);
                long endTime = System.currentTimeMillis();
                long beginTime = endTime-(1000);
                List<UsageStats> usageStats = usageStatsManager.queryUsageStats(UsageStatsManager.INTERVAL_DAILY, beginTime, endTime);
                if (usageStats!=null){
                    for (UsageStats usageStat:usageStats){
                        if (usageStat.getPackageName().contains("com.whatsapp")){
                            editor.putLong(WHATSAPP_COUNTER, usageStat.getTotalTimeInForeground());
                        }
                        if (usageStat.getPackageName().contains("com.discord")){
                            editor.putLong(DISCORD_COUNTER, usageStat.getTotalTimeInForeground());
                        }
                        editor.apply();
                    }
                }

            }
        };
        Timer detectAppTimer = new Timer();
        detectAppTimer.scheduleAtFixedRate(detectApp, 0 , 1000);
        return super.onStartCommand(intent, flags, startId);
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
