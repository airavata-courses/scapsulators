package com.ads.caching.repository;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.CachePut;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import com.ads.caching.entity.NASAData;


@Service
public class NASADao {
	
	@Autowired
	public RedisTemplate redisTemplate;
	static final String HASH_KEY = "NASAData";
	
	public void saveRedisObject(String key, String data) {
        try {
            final HashOperations hashOperations = redisTemplate.opsForHash();
            hashOperations.put(HASH_KEY, key, data);
        } catch (Exception e) {
            System.out.println("Unable to save object to REDIS cache, exception: ");
            e.printStackTrace();
        }
    }
	
	
	
	public String findCacheableObjectByKey(String id) {
        try {
            final HashOperations hashOperations = redisTemplate.opsForHash();
            return (String) hashOperations.get(HASH_KEY, id);
        } catch (Exception e) {
        	System.out.println("Unable to retrieve object from REDIS cache, exception: ");
        	e.printStackTrace();
        }
        return null;
    }

	

}
