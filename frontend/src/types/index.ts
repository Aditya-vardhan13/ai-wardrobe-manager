// Wardrobe Manager Types

export interface ClothingItem {
  id: string;
  user_id: string;
  name: string;
  description: string;
  category: ClothingCategory;
  color: string;
  image_url: string;
  created_at: string;
  updated_at: string;
  embedding?: number[];
}

export type ClothingCategory =
  | 'shirt'
  | 'pants'
  | 'jeans'
  | 'shorts'
  | 'dress'
  | 'skirt'
  | 'jacket'
  | 'sweater'
  | 'shoes'
  | 'accessories'
  | 'other';

export interface SimilarityResult {
  item: ClothingItem;
  similarity_score: number;
  match_percentage: number;
}

export interface User {
  id: string;
  email: string;
  name?: string;
  avatar_url?: string;
}

export interface UploadResponse {
  success: boolean;
  item?: ClothingItem;
  error?: string;
}
