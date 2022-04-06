package com.ads.caching.config;

import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.repository.configuration.EnableRedisRepositories;
import org.springframework.data.redis.serializer.JdkSerializationRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
@EnableRedisRepositories
public class RedisConfig {
	@Bean
	public RedisTemplate getRedisTemplate(LettuceConnectionFactory lettuceConnectionFactory) {
	    RedisTemplate<Object, Object> redisTemplate = new RedisTemplate<>();
	    redisTemplate.setConnectionFactory(lettuceConnectionFactory);
	    redisTemplate.setDefaultSerializer(new StringRedisSerializer());
	    redisTemplate.setHashValueSerializer(new JdkSerializationRedisSerializer());
	    redisTemplate.setEnableTransactionSupport(true);
	    redisTemplate.afterPropertiesSet();
	    return redisTemplate;
	}

	

	@Bean
	public LettuceConnectionFactory connectionFactory() {
	    LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory();
	    connectionFactory.setHostName("redis");
	    connectionFactory.setPort(6379);
	    return connectionFactory;
	}
	
	

}
