const { response } = require('express');
const request = require('supertest');
const app = require('../server');


describe('Get Weather', () => {
    it('GET /api/getimg --> image success',()=> {
        return request(app).get('/api/getimg').expect('Content-Type',/json/).expect(200); });
    
});