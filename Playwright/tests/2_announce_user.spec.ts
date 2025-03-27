import { test, expect } from '@playwright/test';

const url = 'https://trenph.vercel.app/';

/**
test.beforeEach(async ({ page }) => {
  await page.goto(url);

  await page.getByText('Announcements').click();
  await page.waitForNavigation();

  await page.getByText('Load more').click();
  await page.getByText('Load more').click();
});

test('lrt 1 announcements', async ({ page }) => {
  await page.isVisible("text='LRT-1'")
});

test('lrt 2 announcements', async ({ page }) => {
  await page.isVisible("text='LRT-2'")
});

test('mrt 3 announcements', async ({ page }) => {
  await page.isVisible("text='MRT-3'")
});
 */