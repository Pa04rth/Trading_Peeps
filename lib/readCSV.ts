import fs from "fs";
import path from "path";
import { parse } from "csv-parse/sync";

export async function getSymbolsFromCSV(): Promise<string[]> {
  const csvPath = path.join(process.cwd(), "api/stock_names_nse.csv");
  const fileContent = fs.readFileSync(csvPath, "utf-8");

  const records = parse(fileContent, {
    columns: true,
    skip_empty_lines: true,
  });

  return records.map((row: { symbol: string }) => row.symbol);
}
