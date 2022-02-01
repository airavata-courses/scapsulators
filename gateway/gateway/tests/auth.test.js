const { response } = require('express');
const request = require('supertest');
const app = require('../server');

describe('Auth APIs', () => {
    it('GET /api/login --> login success',()=> {
        return request(app).post('/api/login').expect('Content-Type',/json/).expect(200)
        .then((response) => {
            expect(response.body.success).toBeTruthy();
        });

    })

    it('GET /api/register --> 400 without tag',()=> {
        return request(app).post('/api/register').expect('Content-Type',/json/).expect(200);

    })

    
    it('GET /api/forgot --> get posts by tag',()=> {

        return request(app).post('/api/forgot').expect('Content-Type',/json/).expect(200)
        .then((response) => {
            expect(response.body.success).toBeTruthy();
            /*
            expect(response.body.posts).toEqual(
                expect.arrayContaining([
                    expect.objectContaining({
                        author: expect.any(String),
                        authorId: expect.any(Number),
                        id: expect.any(Number),
                        likes: expect.any(Number),
                        popularity: expect.any(Number),
                        reads: expect.any(Number),
                        tags: expect.any(Array),
                    })
                ])
            ) */
        });

    })



})

