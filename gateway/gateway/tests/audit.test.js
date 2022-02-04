const { response } = require('express');
const request = require('supertest');
const app = require('../server');


describe('Get Audit', () => {
    it('GET /api/getaudit --> audit success',()=> {
        return request(app).get('/api/getaudit').expect('Content-Type',/json/).expect(200); });
    
});

describe('Save Audit', () => {
    it('GET /api/getaudit --> audit success',()=> {
        return request(app).post('/api/saveaudit').expect('Content-Type',/json/).expect(200); });
    
});