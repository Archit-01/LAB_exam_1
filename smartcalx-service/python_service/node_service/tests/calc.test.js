const request = require('supertest');
const app = require('../index');

describe('GET /add', () => {
  test('default 0', async () => {
    const res = await request(app).get('/add');
    expect(res.statusCode).toBe(200);
    expect(res.body.result).toBe(0);
  });

  test('adds numbers', async () => {
    const res = await request(app).get('/add?a=1.5&b=2.5');
    expect(res.statusCode).toBe(200);
    expect(res.body.result).toBeCloseTo(4.0);
  });
});
