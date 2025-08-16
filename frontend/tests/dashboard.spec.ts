import { test, expect } from '@playwright/test';

test('login and query workflow', async ({ page }) => {
  await page.goto('http://localhost:3000');
  await page.fill('input[placeholder="Username"]', 'admin');
  await page.fill('input[placeholder="Password"]', 'password');
  await page.click('button:has-text("Login")');
  await expect(page.locator('text=Multi-DB NL Query Engine Dashboard')).toBeVisible();
  await page.fill('input[placeholder="Ask a question..."]', 'show all customers');
  await page.click('button:has-text("Ask")');
  await expect(page.locator('text=Sample')).toBeVisible();
});

test('responsive layout', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('http://localhost:3000');
  await expect(page.locator('input[placeholder="Username"]')).toBeVisible();
});
